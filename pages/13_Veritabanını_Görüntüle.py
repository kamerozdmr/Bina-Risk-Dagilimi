import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


import sys
sys.path.append("../")
from sql.read_database import ConnectDatabase, readBetonarme, EndConnection


st.set_page_config(page_title="Bina Risk Dağılımı", page_icon="figures/logo.png")

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)


# auth kontrol et 
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None

if st.session_state["authentication_status"] == False:
    st.warning("Devam etmek için Ana Sayfaya dönüp giriş yapınız.")
    # Yan bar bilgi mesajı
    st.sidebar.warning("Giriş yapılmadı")

if st.session_state["authentication_status"] == None:
    st.warning("Devam etmek için Ana Sayfaya dönüp giriş yapınız.")
    # Yan bar bilgi mesajı
    st.sidebar.warning("Giriş yapılmadı")



if st.session_state["authentication_status"]:

    st.title("Veritabanını Görüntüle")

    bina_adet_option = st.selectbox(
    "Gösterilecek en son eklenen bina adedini seçin.",
    (5, 10, 20, 50))

    colorbar_option = st.selectbox(
    "Haritada gösterilecek colorbar verisini seçin.",
    ("performans_puani","kat_adedi", "taban_puani", "olumsuzluk_puani", "yapisal_sistem_puani"))

    st.write("---")
    bina_adet = int(bina_adet_option)
    baglan_submit = st.button("Bağlan")


    col1, col2, col3 = st.columns([1, 1, 1])
    if baglan_submit:
        #st.success("Veritabanına bağlandı.")
        st.session_state["df_ss"]  = readBetonarme()
        df = st.session_state["df_ss"]
        st.success(f"Toplam {df.shape[0]} binaya ulaşıldı.")



    # Bağlan butonu Raise error
    if "df_ss" not in st.session_state:
        st.warning("Veritabanına bağlanın.")
    
    
    else:
        st.write("---")
        with col1:
            tablo_submit = st.button("Tabloda göster")

        with col2:
            figur_submit = st.button("Haritada göster")

        with col3:
            figur_all_submit = st.button("Tüm binaları haritada göster")


        if tablo_submit:
            st.session_state["df_trimmed"] = st.session_state["df_ss"].tail(bina_adet)
            st.dataframe(st.session_state["df_trimmed"])  
                


        if figur_submit:
            st.session_state["df_trimmed"] = st.session_state["df_ss"].tail(bina_adet)

            st.session_state["df_map_trimmed"] = st.session_state["df_trimmed"].loc[:, ("enlem", "boylam", "kat_adedi", "performans_puani", "no", "yapi_no", "taban_puani", "olumsuzluk_puani", "yapisal_sistem_puani")]
            #st.session_state["df_map_trimmed"].rename(columns = {'enlem':'lat', 'boylam':'lon'}, inplace = True)
            
            #st.map(st.session_state["df_map_trimmed"], zoom=13)

            # Plotly Map
            fig = px.scatter_mapbox(st.session_state["df_map_trimmed"], lat="enlem", lon="boylam", hover_name="yapi_no", hover_data=["kat_adedi", "performans_puani", "no"],
                                    color=str(colorbar_option), color_continuous_scale=px.colors.sequential.Bluered, zoom=14, height=540)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            
            st.plotly_chart(fig)


        if figur_all_submit:
            st.session_state["df_map"] = st.session_state["df_ss"].loc[:, ("enlem", "boylam", "kat_adedi", "performans_puani", "no", "yapi_no", "taban_puani", "olumsuzluk_puani", "yapisal_sistem_puani")]
            
            # Plotly Map
            fig = px.scatter_mapbox(st.session_state["df_map"], lat="enlem", lon="boylam", hover_name="yapi_no", hover_data=["kat_adedi", "performans_puani", "no"],
                                    color=str(colorbar_option), color_continuous_scale=px.colors.sequential.Bluered, zoom=14, height=540)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            
            st.plotly_chart(fig)



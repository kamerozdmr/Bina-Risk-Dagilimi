import streamlit as st
from PIL import Image

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

    # İlerlemeyi gösteren bar ekle
    prg_percent = 80 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Yapı Nizamı/Bitişik Binalarla Döşeme Seviyeleri")

    # Kayıt butonu Raise error
    if "sds_ss" not in st.session_state:
        st.error("Sds değeri kaydedilemedi.", icon="🚨")
        st.stop()
    else:
        if st.session_state["sds_ss"] == "clicked":
            pass
        elif st.session_state["sds_ss"] == "error":
            st.error("Sds değeri hatalı, kaydedilemedi.", icon="🚨")
            st.stop()

            
    if st.session_state["bina_tipi"] == "Betonarme" or "Yığma":
        #Betonarme bina tipinin seçildiği durum

        st.subheader("Açıklama")
        st.write("Bitişik binaların konumları deprem \
                performansını çarpışma nedeniyle etkileyebilmektedir. Kenarda yer alan binalar bu durumdan \
                en olumsuz etkilenmekte, bitişik bina ile kat seviyeleri farklıysa bu olumsuzluk daha da \
                artmaktadır. Çarpışma etkisinin söz konusu olduğu durumlar dışarıdan yapılacak gözlemler ile \
                belirlenecektir. Yapı nizam durumu ve bitişik binalarla döşeme seviyesi durumu birlikte \
                değerlendirilecektir."
                )

        image = Image.open("./figures/nizam_durumu.jpg")
        st.image(image, width = 240)

        nizam_durumu = st.radio(
            "Yapının nizam durumunu seçiniz.",
            ("Ayrık", "Bitişik"))

        st.session_state["nizam_durumu"] = nizam_durumu


        if "nizam_konumu" not in st.session_state:
            st.session_state["nizam_konumu"] = " "

        if "doseme_seviyesi" not in st.session_state:
            st.session_state["doseme_seviyesi"] = " "

        st.write("---")
        ########################################

        if st.session_state["nizam_durumu"] == "Bitişik":
            nizam_konumu = st.radio(
                "Bitişik yapının konumunu seçiniz.",
                ("Ortada", "Köşede"))

            st.session_state["nizam_konumu"] = nizam_konumu 

            st.write("---")
            ########################################

            image = Image.open("./figures/doseme_seviyesi.jpg")
            st.image(image, width = 420)

            doseme_seviyesi = st.radio(
                "Bitişik yapının döşeme seviyesi durumunu seçiniz.",
                ("Aynı", "Farklı"))

            st.session_state["doseme_seviyesi"] = doseme_seviyesi

        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)
        


    elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
        st.write("Bina tipini seçiniz.")
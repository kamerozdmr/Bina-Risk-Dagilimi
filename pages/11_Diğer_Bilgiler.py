import streamlit as st

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
    prg_percent = 90 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Diğer Bilgiler")

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


    st.write("Verilen parametreler dışında bina hakkında girmek istediğiniz bilgileri aşağıdaki alana yazabilirsiniz.")

    if "diger_bilgiler" not in st.session_state:
        st.session_state["diger_bilgiler"] = ""


    diger_bilgiler = str(st.text_area(st.session_state["diger_bilgiler"], height=200))
    coord_submit = st.button("Kaydet")

    if coord_submit:
        st.session_state["diger_bilgiler"] = diger_bilgiler
        st.success("Kaydedildi.")

    # İlerleme barını güncelle
    progress_bar.progress(prg_percent+10)

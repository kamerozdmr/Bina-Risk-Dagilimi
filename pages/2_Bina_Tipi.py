import streamlit as st
from PIL import Image


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
    prg_percent = 0 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Bina Tipi/Formu")

    image = Image.open("./figures/yapi-tipi-gorsel.jpg")
    st.image(image)


    bina_tipi = st.radio(
        "Bina tipinizi seçiniz.",
        ("Betonarme", "Yığma"))

    st.session_state["bina_tipi"] = bina_tipi

    # İlerleme barını güncelle
    progress_bar.progress(prg_percent+10)

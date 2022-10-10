import streamlit as st
from PIL import Image

st.title("Bina Tipi/Formu")

image = Image.open("./figures/yapi-tipi-gorsel.jpg")
st.image(image, caption='Yapı tipi örneği', width = 720)

bina_tipi = st.radio(
    "Bina tipinizi seçiniz.",
    ("Betonarme", "Yığma"))

st.session_state["bina_tipi"] = bina_tipi



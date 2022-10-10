import streamlit as st
import pandas as pd

st.title("Coğrafi Koordinatlar")
st.subheader("Açıklama")
st.write("Türkiye Deprem Tehlike Haritası koordinat sistemiyle uyumlu olarak belirlenmelidir. DATUM WGS 1984")


if "lat_input" not in st.session_state:
    st.session_state["lat_input"] = ""

if "lon_input" not in st.session_state:
    st.session_state["lon_input"] = ""


lat_input = st.text_input("Enlem", st.session_state["lat_input"])
lon_input = st.text_input("Boylam", st.session_state["lon_input"])
coord_submit = st.button("Kaydet")

if coord_submit:
    st.session_state["lat_input"] = float(lat_input)
    st.session_state["lon_input"] = float(lon_input)
    st.write("Kaydedildi")


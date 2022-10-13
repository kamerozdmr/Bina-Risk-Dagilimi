import streamlit as st
from geopy.geocoders import Nominatim

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

# İlerlemeyi gösteren bar ekle
prg_percent = 30 # İlerleme yüzdesi
progress_bar = st.progress(prg_percent)

# Yan bar bilgi mesajı
st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

st.title("Coğrafi Koordinatlar")
#st.subheader("Açıklama")
st.write("Türkiye Deprem Tehlike Haritası koordinat sistemiyle uyumlu olarak belirlenmelidir. DATUM WGS 1984")


if "enlem" not in st.session_state:
    st.session_state["enlem"] = ""

if "boylam" not in st.session_state:
    st.session_state["boylam"] = ""

if "adres" not in st.session_state:
    st.session_state["adres"] = ""

enlem = (st.text_input("Enlem", st.session_state["enlem"]))
boylam = (st.text_input("Boylam", st.session_state["boylam"]))
coord_submit = st.button("Kaydet")

if coord_submit:
    st.session_state["enlem"] = float(enlem)
    st.session_state["boylam"] = float(boylam)

    # Reverse Geocode, koordinatlardan adres bilgisini elde et
    geolocator = Nominatim(user_agent="Seismic_Risk_For_Buildings")
    location = geolocator.reverse(f"{enlem}, {boylam}")
    st.session_state["adres"] = location.address
    adres = st.session_state["adres"]
  
    st.success(f"Kaydedildi.\n\nAdres : {adres}")

    # İlerleme barını güncelle
    progress_bar.progress(prg_percent+10)


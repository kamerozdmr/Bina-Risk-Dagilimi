import streamlit as st
from geopy.geocoders import Nominatim

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
    prg_percent = 30 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Coğrafi Koordinatlar")
    #st.subheader("Açıklama")
    st.write("Türkiye Deprem Tehlike Haritası koordinat sistemiyle uyumlu olarak belirlenmelidir. DATUM WGS 1984")

    # Kayıt butonu Raise error
    if "bilgi_ss" not in st.session_state:
        st.error("Yapı bilgileri kaydedilemedi.", icon="🚨")
        st.stop()
    else:
        if st.session_state["bilgi_ss"] == "clicked":
            pass
        elif st.session_state["bilgi_ss"] == "error":
            st.error("Yapı bilgileri hatalı, kaydedilemedi.", icon="🚨")
            st.stop()


    if "enlem" not in st.session_state:
        st.session_state["enlem"] = 0

    if "boylam" not in st.session_state:
        st.session_state["boylam"] = 0

    if "adres" not in st.session_state:
        st.session_state["adres"] = ""

    enlem = float(st.text_input("Enlem", st.session_state["enlem"]))
    boylam = float(st.text_input("Boylam", st.session_state["boylam"]))
    coord_submit = st.button("Kaydet")

    if coord_submit:
        if 35.8<=enlem<=42.1 and 25.5<=boylam<=44.5:
            st.session_state["enlem"] = float(enlem)
            st.session_state["boylam"] = float(boylam)

            # Reverse Geocode, koordinatlardan adres bilgisini elde et
            geolocator = Nominatim(user_agent="Seismic_Risk_For_Buildings")
            location = geolocator.reverse(f"{enlem}, {boylam}")
            st.session_state["adres"] = location.address
            adres = st.session_state["adres"]
        
            st.success(f"Kaydedildi.\n\nAdres : {adres}")

            st.session_state["coord_ss"] = "clicked"

            # İlerleme barını güncelle
            progress_bar.progress(prg_percent+10)
        
        
        else:
            st.error("Türkiye sınırları içerisinde koordinat giriniz.")
            st.session_state["coord_ss"] = "error"
            


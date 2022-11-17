import streamlit as st
import sys
sys.path.append("../")
from spektral_ivme.sds import getAccCoeff, CalculateSds, CalculatEz, rounder

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
    prg_percent = 40 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Deprem Tehlike Bölgesi")

    st.subheader("Zemin Sınıfı")

    if "zemin_sinifi" not in st.session_state:
        st.session_state["zemin_sinifi"] = ""

    zemin_sinifi = str(st.radio(
            "Zemin sınıfını seçiniz.",
            ("ZA", "ZB", "ZC", "ZD", "ZE")))

    st.session_state["zemin_sinifi"] = zemin_sinifi

    st.write("---")
    ########################################
    st.subheader("Spektral İvme Katsayısı")

    st.write("Deprem Tehlike Bölgesi, belirtilen deprem yer hareketi düzeyleri ve zemin sınıfları ile uyumlu olarak \
            esaslarda anlatıldığı şekilde dikkate alınacaktır. Yöntemde DD-2 deprem yer hareketi \
            düzeyi kullanılacak ve kısa periyot tasarım spektral ivme katsayısı (Sds) parametre değeri yürürlükte olan Türkiye Deprem Tehlike \
            Haritasından alınacaktır. Parametre değeri ile zemin sınıfları arasındaki ilişki kullanılarak \
            deprem tehlike bölgeleri belirlenecektir.")

    col1, col2 = st.columns([1, 1])
    with col1:
        

        if "ivme_katsayisi" not in st.session_state:
            st.session_state["ivme_katsayisi"] = 0

        ivme_katsayisi = float(st.text_input("DD-2 depremi kısa periyot ivme katsayısını giriniz.", st.session_state["ivme_katsayisi"]))

        coord_submit1 = st.button("Kaydet")
        
    
    ########################################

    with col2:
        # Sds yaklaşık hesapla
        st.write("Yaklaşık olarak Sds değerini hesapla.")
        coord_submit2 = st.button("Yaklaşık Hesapla")

        st.write("[Kesin değer için sayfayı ziyaret edin.](https://tdth.afad.gov.tr/)")

        if coord_submit2:
            if st.session_state["enlem"] and st.session_state["boylam"] != 0:
                Yaklasik_Sds = getAccCoeff(st.session_state["enlem"], st.session_state["boylam"], st.session_state["zemin_sinifi"])

                st.success(f"Sds : {Yaklasik_Sds[1]}")
            
            else:
                st.warning("Koordinat değerleri bulunamadı.")
 


    if coord_submit1:
        if 0 < ivme_katsayisi <= 4:
            st.session_state["ivme_katsayisi"] = ivme_katsayisi
            st.session_state["zemin_sinifi"] = zemin_sinifi
            st.success(f"Kaydedildi.\n\nSds : {ivme_katsayisi}\n\nZemin Sınıfı : {zemin_sinifi}")

            # İlerleme barını güncelle
            progress_bar.progress(prg_percent+10)
        else:
            st.error("Geçerli ivme katsayısı değeri giriniz.")


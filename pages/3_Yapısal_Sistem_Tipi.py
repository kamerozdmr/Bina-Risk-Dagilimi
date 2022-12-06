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
    prg_percent = 10 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Yapısal Sistem Tipi")

    if st.session_state["bina_tipi"] == "Betonarme":
        #Betonarme bina tipinin seçildiği durum

        st.write("Binanın taşıyıcı sistemi belirlenerek, betonarme çerçeve (BAÇ) ile \
                betonarme çerçeve ve perde (BAÇP) sistemlerinden biri olarak seçilecektir. Bodrum varsa \
                bodrum kat içinden, dükkân varsa dükkân içinden tespit edilmesi uygun olacaktır. Tespit \
                edilemiyor ise BAÇ seçilmesi uygun olacaktır."
                )

        image = Image.open("./figures/sistem_turu_gorsel.jpg")
        st.image(image)

        sistem_tipi = st.radio(
            "Yapısal sistem tipini seçiniz.",
            ("Betonarme çerçeve (BAÇ)", "Betonarme çerçeve ve perde (BAÇP)"))

        st.session_state["sistem_tipi"] = sistem_tipi
        
        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)



    elif  st.session_state["bina_tipi"] == "Yığma":
        #Diğer durum olan yığma bina tipinin seçildiği durum

        st.subheader("Açıklama")
        st.write("Binanın taşıyıcı sistemi belirlenerek, donatısız yığma, kuşatılmış yığma, \
                donatılı yığma ve karma (yığma duvar + betonarme çerçeve) sistemlerinden biri yapı sistemi \
                olarak seçilecektir."
                )

        image = Image.open("./figures/yigma_bina_turu.jpg")
        st.image(image, width = 720)

        sistem_tipi = st.radio(
            "Yapısal sistem tipini seçiniz.",
            ("Donatısız Yığma", "Donatılı Yığma", "Kuşatılmış Yığma", "Karma"))

        st.session_state["sistem_tipi"] = sistem_tipi

        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)


    elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
        # Raise error
        st.error("Bina tipini seçiniz.", icon="🚨")

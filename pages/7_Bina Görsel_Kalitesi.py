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
    prg_percent = 50 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Bina Görsel Kalitesi")

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


    if st.session_state["bina_tipi"] == "Betonarme":
        #Betonarme bina tipinin seçildiği durum

        #st.subheader("Açıklama")
        st.write("Binanın görünen kalitesi malzeme ve işçilik kalitesine ve binanın bakımına \
                verilen önemi yansıtır. Binanın görünen kalitesi iyi(0), orta(1) ve kötü(2) olarak sınıflandırılacaktır. "
                )

        ########################################
        if "gorsel_kalite" not in st.session_state:
            st.session_state["gorsel_kalite"] = ""

        gorsel_kalite = st.slider("Bina görsel kalitesini seçiniz.", 0, 2, 0)
        st.session_state["gorsel_kalite"] = int(gorsel_kalite)

        if st.session_state["gorsel_kalite"] == 0:
            st.markdown("Bina görsel kalitesi **İYİ**")
        elif st.session_state["gorsel_kalite"] == 1:
            st.markdown("Bina görsel kalitesi **ORTA**")
        elif st.session_state["gorsel_kalite"] == 2:
            st.markdown("Bina görsel kalitesi **KÖTÜ**")

        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)


    elif  st.session_state["bina_tipi"] == "Yığma":
        #Diğer durum olan yığma bina tipinin seçildiği durum
        #st.subheader("Açıklama")
        st.write("Malzeme türü ve kalitesi ile yığma duvar işçiliği ayrı ayrı \
                kontrol edilerek, bu tespitlerin her ikisi için ayrı ayrı İyi(0), Orta(1) ve Kötü(2) olarak sınıflandırma \
                yapılacaktır. Ayrıca, mevcut hasar olup olmadığı tespit edilecek ve binada hasar Var veya Yok \
                şeklinde tespit yapılacaktır."
                )

        ########################################
        if "malzeme_kalite" not in st.session_state:
            st.session_state["malzeme_kalite"] = ""

        malzeme_kalite = st.slider("Malzeme kalitesini seçiniz.", 0, 2, 0)
        st.session_state["malzeme_kalite"] = int(malzeme_kalite)

        if st.session_state["malzeme_kalite"] == 0:
            st.markdown("Malzeme kalitesi **İYİ**")
        elif st.session_state["malzeme_kalite"] == 1:
            st.markdown("Malzeme kalitesi **ORTA**")
        elif st.session_state["malzeme_kalite"] == 2:
            st.markdown("Malzeme kalitesi **KÖTÜ**")

        st.write("---")
        ########################################

        if "duvar_isciligi" not in st.session_state:
            st.session_state["duvar_isciligi"] = ""

        duvar_isciligi = st.slider("Yığma duvar işçiliğini değerlendiriniz.", 0, 2, 0)
        st.session_state["duvar_isciligi"] = int(duvar_isciligi)

        if st.session_state["duvar_isciligi"] == 0:
            st.markdown("Yığma duvar işçiliği **İYİ**")
        elif st.session_state["duvar_isciligi"] == 1:
            st.markdown("Yığma duvar işçiliği **ORTA**")
        elif st.session_state["duvar_isciligi"] == 2:
            st.markdown("Yığma duvar işçiliği **KÖTÜ**")

        st.write("---")
        ########################################

        if "bina_hasari" not in st.session_state:
            st.session_state["bina_hasari"] = ""

        bina_hasari = st.radio(
        "Binada mevcut hasar var mı?",
        ("Yok", "Var"))

        st.session_state["bina_hasari"] = bina_hasari

        st.write("---")
        ########################################
        if "cati_malzemesi" not in st.session_state:
            st.session_state["cati_malzemesi"] = ""

        cati_malzemesi = st.radio(
        "Bina çatı malzemesini seçiniz.",
        ("Kiremit, Saç veya Beton", "Toprak"))

        st.session_state["cati_malzemesi"] = cati_malzemesi



        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)

        

    elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
        st.write("Bina tipini seçiniz.")
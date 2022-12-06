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
    prg_percent = 60 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

    st.title("Düşeyde Düzensizlikler")
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

        ########################################
        st.subheader("Düşeyde Düzensizlik Durumu")
        st.write("Düşeyde devam etmeyen çerçeve ve değişen kat alanlarının etkisini \
                yansıtmak amacıyla dikkate alınacaktır. Bina yüksekliği boyunca devam etmeyen kolonlar \
                veya perdeler düşeyde düzensizlik oluşturur."
                )

        image = Image.open("./figures/duseyde_duzensizlik_gorsel.jpg")
        st.image(image)

        duseyde_duzensizlik = st.radio(
            "Binada düşeyde düzensizlik durumunu var mı?",
            ("Yok", "Var"))

        st.session_state["duseyde_duzensizlik"] = duseyde_duzensizlik

        st.write("---")
        ########################################

        st.subheader("Yumuşak/Zayıf Kat Durumu")
        st.write("Kat yüksekliği farkının yanı sıra katlar arası belirgin rijitlik farkı da \
                dikkate alınarak gözlemsel olarak belirlenecektir."
                )

        image = Image.open("./figures/zayif_kat.jpg")
        st.image(image)

        yumusak_kat = st.radio(
            "Binada yumuşak/zayıf kat durumu var mı?",
            ("Yok", "Var"))

        st.session_state["yumusak_kat"] = yumusak_kat

        st.write("---")
        ########################################

        st.subheader("Ağır Çıkma Durumu")
        st.write("Zemine oturan kat alanı ile zemin üstündeki kat alanı arasındaki farklılık belirlenecektir."
                )

        image = Image.open("./figures/agir_cikma.jpg")
        st.image(image)

        agir_cikma = st.radio(
            "Binada ağır çıkma var mı?",
            ("Yok", "Var"))

        st.session_state["agir_cikma"] = agir_cikma
    

        st.write("---")
        ########################################

        st.subheader("Kısa Kolon Etkisi")
        st.write("Bu aşamada sadece dışarıdan gözlenen kısa kolonlar değerlendirmede dikkate alınacaktır."
                )

        image = Image.open("./figures/kisa_kolon.jpg")
        st.image(image, width = 240)

        kisa_kolon = st.radio(
            "Binada kısa kolon etkisi var mı?",
            ("Yok", "Var"))

        st.session_state["kisa_kolon"] = kisa_kolon

        st.write("---")
        ########################################

        st.subheader("Tabii Zemin Eğimi")
        st.write("Belli bir eğimin üzerindeki yamaçlarda inşa edilmiş binalarda bu etki \
                dikkate alınacaktır. Tabii zemin eğimi 30º nin altında ise tepe yamaç etkisi olmadığı, tabii zemin \
                eğimi 30º nin üzerinde ise tepe yamaç etkisi olduğu kabul edilecektir."
                )

        zemin_egimi = st.radio(
            "Zemin eğimi etkisi var mı?",
            ("Yok", "Var"))

        st.session_state["zemin_egimi"] = zemin_egimi

        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)



    elif  st.session_state["bina_tipi"] == "Yığma":
        #Diğer durum olan yığma bina tipinin seçildiği durum
        st.title("Düşeyde Düzensizlikler ve Düzlem Dışı Davranış Olumsuzlukları")
        ########################################
        st.subheader("Düşey Boşluk Düzensizliği")
        st.write("Binada bulunan kapı ve pencere boşluklarının düşey yönde \
                yerleşimine göre düşey doğrultudaki boşluk düzeni; Düzenli(0), Az Düzenli(1) ve Düzensiz(2) olarak \
                sınıflandırılacaktır."
                )

        image = Image.open("./figures/dusey_bosluk_duzeni_yigma.jpg")
        st.image(image, width=360)

        if "dusey_bosluk_duzensizligi" not in st.session_state:
            st.session_state["dusey_bosluk_duzensizligi"] = ""
            
        dusey_bosluk_duzensizligi = st.slider("Bina düşey boşluk düzensizliği seviyesini seçiniz.", 0, 2, 0)
        st.session_state["dusey_bosluk_duzensizligi"] = int(dusey_bosluk_duzensizligi)

        if st.session_state["dusey_bosluk_duzensizligi"] == 0:
            st.markdown("Bina görsel kalitesi **Düzenli**")
        elif st.session_state["dusey_bosluk_duzensizligi"] == 1:
            st.markdown("Bina görsel kalitesi **Az Düzenli**")
        elif st.session_state["dusey_bosluk_duzensizligi"] == 2:
            st.markdown("Bina görsel kalitesi **Düzensiz**")

        st.write("---")
        ########################################

        st.subheader("Cepheye Göre Kat Sayısı Farklılığı")
        st.write("Binanın farklı cephelerinin farklı kat sayısına sahip olması durumu \
                tespit edilecektir."
                )

        image = Image.open("./figures/cephe_kat_farkliligi.jpg")
        st.image(image)

        cephe_kat_farkliligi = st.radio(
            "Cepheye göre kat farklılığı var mı?",
            ("Yok", "Var"))

        st.session_state["cephe_kat_farkliligi"] = cephe_kat_farkliligi

        st.write("---")
        ########################################

        st.subheader("Yumuşak/Zayıf Kat Durumu")
        st.write("Kat yüksekliği farkının yanı sıra katlar arası belirgin rijitlik farkı da \
                dikkate alınarak gözlemsel olarak belirlenecektir."
                )

        image = Image.open("./figures/zayif_kat_yigma.jpg")
        st.image(image, width= 400)

        yumusak_kat = st.radio(
            "Binada yumuşak/zayıf kat durumu var mı?",
            ("Yok", "Var"))

        st.session_state["yumusak_kat"] = yumusak_kat

        st.write("---")
        ########################################

        st.title("Düzlem Dışı Davranış Olumsuzlukları")

        st.write("Yığma bina duvarlarının düzlem dışı davranış gösterme \
                eğiliminde olup olmadığı belirlenecektir. Yığma binalarda düzlem dışı davranışı tetikleyen ve \
                genellikle bina dışından tespit edilebilen olumsuzluklar aşağıda verilmiştir."
                )
        ########################################
        st.subheader("Duvar-Duvar ve Duvar-Döşeme Bağlantıları")
        st.write("Duvar-duvar ve duvar-döşeme bağlantılarının zayıf olması, bağlantıların bulunduğu yerde \
                çatlak veya hasar olması, hatıl bulunmaması gibi durumlar dikkate alınacaktır."
                )

        duv_duv_baglanti = st.radio(
            "Duvar-duvar bağlantı durumunu belirtiniz.",
            ("İyi", "Kötü"))

        st.session_state["duv_duv_baglanti"] = duv_duv_baglanti

        duv_dos_baglanti = st.radio(
            "Duvar-döşeme bağlantı durumunu belirtiniz.",
            ("İyi", "Kötü"))

        st.session_state["duv_dos_baglanti"] = duv_dos_baglanti
        
        
        st.write("---")
        ########################################
        st.subheader("Döşeme Tipi")
        st.write("Yapının döşeme tipine göre rijit diyafram oluşumu incelenecektir.")

        doseme_tipi = st.radio(
            "Binanın döşeme tipini seçiniz.",
            ("Betonarme", "Ahşap veya Volto"))

        st.session_state["doseme_tipi"] = doseme_tipi

        st.write("---")
        ########################################
        st.subheader("Harç Malzemesi")
        st.write("Harç kalitesinin çok düşük olması ya da hiç harç olmaması durumu incelenecektir.")

        harc_malzemesi = st.radio(
            "Harç malzemesini seçiniz.",
            ("Çimento", "Kireç, Çamur veya Yok"))

        st.session_state["harc_malzemesi"] = harc_malzemesi


        # İlerleme barını güncelle
        progress_bar.progress(prg_percent+10)

    elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
        st.write("Bina tipini seçiniz.")
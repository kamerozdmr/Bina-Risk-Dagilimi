import streamlit as st
from PIL import Image
from tempfile import NamedTemporaryFile

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
    prg_percent = 20 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Yan bar bilgi mesajı
    st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")


    if st.session_state["bina_tipi"] == "Betonarme":
        #Betonarme bina tipinin seçildiği durum

        st.title("Yapı Bilgileri")

        st.subheader("Bina Fotoğrafı")
        st.write("Binanın ön cephesinden ve binayı temsil edebilecek net bir fotoğraf ekleyiniz.")

        if "bina_fotograf" not in st.session_state:
            st.session_state["bina_fotograf"] = ""

        col1, col2 = st.columns([2, 1])
        with col1:
            image = st.file_uploader("Fotoğraf seçiniz (.jpg, .jpeg, .png)", type = ["jpg", "jpeg", "png"] )

        with col2:
            if image is not None:
                st.session_state["bina_fotograf"] = image
                st.image(image)


        st.write("---")
        ########################################

        st.subheader("Serbest Kat Adedi")
        st.write("Bu yöntem 1 ila 7 katlı betonarme binalar ve 1 ila 5 katlı yığma binalar için kullanılabilir.  \
                Serbest kat adedi aşağıdaki görsel dikkate alınarak tespit edilecektir.")

        image = Image.open("./figures/kat_adedi_betonarme.jpg")
        st.image(image, width=280)

        if "kat_adedi" not in st.session_state:
            st.session_state["kat_adedi"] = 0

        kat_adedi = st.text_input("Serbest kat adedini giriniz.", st.session_state["kat_adedi"])

        st.write("---")
        ########################################

        st.subheader("Bina Yapım Yılı")
        yapim_yili = str(st.radio(
            "Ruhsata göre binanın yapım yılı aralığını seçiniz.",
            ("<2000", "2000-2007", "2008-2018", ">2018")))
        
        
        if "yapim_yili" not in st.session_state:
            st.session_state["yapim_yili"] = ""

        st.session_state["yapim_yili"] = yapim_yili

        st.write("---")
        ########################################   

        st.subheader("Yapı Numarası")
        st.write("Adres kayıt sisteminden alınabilecek yapı numarasını giriniz.")
        st.write("[Adres Kayıt Sistemi](https://adres.nvi.gov.tr/VatandasIslemleri/AdresSorgu)")
        if "yapi_no" not in st.session_state:
            st.session_state["yapi_no"] = ""

        yapi_no = st.text_input("Yapı numarasını giriniz.", st.session_state["yapi_no"])
        st.session_state["yapi_no"] = yapi_no

        ########################################
        coord_submit = st.button("Kaydet")
        if coord_submit:
            if 1 <= int(kat_adedi) <= 7: 
                st.session_state["kat_adedi"] = int(kat_adedi)
                st.session_state["yapim_yili"] = yapim_yili
                st.session_state["yapi_no"] = yapi_no
                st.success("Kaydedildi.")
                
                # İlerleme barını güncelle
                progress_bar.progress(prg_percent+10)

            else:
                st.error("Betonarme bina için geçerli kat adedi veya yapım yılı giriniz.")

        ########################################


    elif  st.session_state["bina_tipi"] == "Yığma":
        #Diğer durum olan yığma bina tipinin seçildiği durum
        
        st.title("Yapı Bilgileri")
            
        st.subheader("Bina Fotoğrafı")
        st.write("Binanın ön cephesinden ve binayı temsil edebilecek net bir fotoğraf ekleyiniz.")

        if "bina_fotograf" not in st.session_state:
            st.session_state["bina_fotograf"] = ""

        col1, col2 = st.columns([2, 1])
        with col1:
            image = st.file_uploader("Fotoğraf seçiniz (.jpg, .jpeg, .png)", type = ["jpg", "jpeg", "png"] )

        with col2:
            if image is not None:
                st.session_state["bina_fotograf"] = image
                st.image(image)

        st.write("---")
        ########################################
        
        st.subheader("Serbest Kat Adedi")
        st.write("Bu yöntem 1 ila 7 katlı betonarme binalar ve 1 ila 5 katlı yığma binalar için kullanılabilir.  \
                Serbest kat adedi aşağıdaki görsel dikkate alınarak tespit edilecektir.")

        image = Image.open("./figures/kat_adedi_yigma.jpg")
        st.image(image, width = 280)

        if "kat_adedi" not in st.session_state:
            st.session_state["kat_adedi"] = 0

        kat_adedi = st.text_input("Serbest kat adedini giriniz.", st.session_state["kat_adedi"])
        
        st.write("---")
        ########################################

        st.subheader("Bina Yapım Yılı")
        yapim_yili = str(st.radio(
            "Ruhsata göre binanın yapım yılı aralığını seçiniz.",
            ("<2000", "2000-2007", "2008-2018", ">2018")))
        
        
        if "yapim_yili" not in st.session_state:
            st.session_state["yapim_yili"] = ""

        st.session_state["yapim_yili"] = yapim_yili

        st.write("---")
        ########################################   

        st.subheader("Yapı Numarası")
        st.write("Adres kayıt sisteminden alınabilecek yapı numarasını giriniz.")
        st.write("[Adres Kayıt Sistemi](https://adres.nvi.gov.tr/VatandasIslemleri/AdresSorgu)")
        if "yapi_no" not in st.session_state:
            st.session_state["yapi_no"] = ""

        yapi_no = st.text_input("Yapı numarasını giriniz.", st.session_state["yapi_no"])
        st.session_state["yapi_no"] = yapi_no
        ########################################


        coord_submit = st.button("Kaydet")
        

        if coord_submit:
            if 1 <= int(kat_adedi) <= 5: 
                st.session_state["kat_adedi"] = kat_adedi
                st.session_state["yapim_yili"] = yapim_yili
                st.session_state["yapi_no"] = yapi_no
                st.success("Kaydedildi.")
                
                # İlerleme barını güncelle
                progress_bar.progress(prg_percent+10)

            else:
                st.error("Yığma bina için geçerli kat adedi veya yapım yılı giriniz.")



        ########################################



    elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
        st.write("Bina tipini seçiniz.")
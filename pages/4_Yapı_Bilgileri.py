import streamlit as st
from PIL import Image
from tempfile import NamedTemporaryFile

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

# İlerlemeyi gösteren bar ekle
prg_percent = 20 # İlerleme yüzdesi
progress_bar = st.progress(prg_percent)

# Yan bar bilgi mesajı
st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")


if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.title("Yapı Bilgileri")
    ########################################
    st.subheader("Serbest Kat Adedi")
    st.write("Bu yöntem 1 ila 7 katlı betonarme binalar ve 1 ila 5 katlı yığma binalar için kullanılabilir.  \
             Serbest kat adedi aşağıdaki görsel dikkate alınarak tespit edilecektir.")

    image = Image.open("./figures/kat_adedi_betonarme.jpg")
    st.image(image, width=300)

    if "kat_adedi" not in st.session_state:
        st.session_state["kat_adedi"] = 0

    kat_adedi = st.text_input("Serbest kat adedini giriniz.", st.session_state["kat_adedi"])


    ########################################
    st.subheader("Bina Yapım Yılı")
    st.write("Ruhsata göre binanın yapım yılını giriniz.")

    if "yapim_yili" not in st.session_state:
        st.session_state["yapim_yili"] = 0

    yapim_yili = st.text_input("Yapım yılını giriniz.", st.session_state["yapim_yili"])
    
    coord_submit = st.button("Kaydet")
    
    ########################################

    if coord_submit:
        if 1 <= int(kat_adedi) <= 7 and 1800<= int(yapim_yili)<= 2022: 
            st.session_state["kat_adedi"] = int(kat_adedi)
            st.session_state["yapim_yili"] = int(yapim_yili)
            st.success("Kaydedildi.")
            
            # İlerleme barını güncelle
            progress_bar.progress(prg_percent+10)

        else:
            st.error("Betonarme bina için geçerli kat adedi veya yapım yılı giriniz.")

    ########################################

    st.subheader("Bina Fotoğrafı")
    st.write("Binanın ön cephesinden ve binayı temsil edebilecek net bir fotoğraf ekleyiniz.")
    col1, col2 = st.columns(2)
    with col1:
        st.set_option('deprecation.showfileUploaderEncoding', False)

        buffer = st.file_uploader("Fotoğraf seçin (.jpg)", type="jpg")
        temp_file = NamedTemporaryFile(delete=False)
        #st.write(temp_file)

    with col2:
        if buffer:
            temp_file.write(buffer.getvalue())
            bina_fotograf = Image.open(temp_file.name)
            st.session_state["bina_fotograf"] = bina_fotograf
            st.image(bina_fotograf)


    ########################################
    


            
        

    


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.subheader("Serbest Kat Adedi")
    st.write("Bu yöntem 1 ila 7 katlı betonarme binalar ve 1 ila 5 katlı yığma binalar için kullanılabilir.  \
             Serbest kat adedi aşağıdaki görsel dikkate alınarak tespit edilecektir.")

    image = Image.open("./figures/kat_adedi_yigma.jpg")
    st.image(image, width = 360)

    if "kat_adedi" not in st.session_state:
        st.session_state["kat_adedi"] = ""

    kat_adedi = st.text_input("Serbest kat adedini giriniz.", st.session_state["kat_adedi"])
    
    st.subheader("Bina Yapım Yılı")
    st.write("Ruhsata göre binanın yapım yılını giriniz.")

    if "yapim_yili" not in st.session_state:
        st.session_state["yapim_yili"] = ""

    yapim_yili = st.text_input("Yapım yılını giriniz.", st.session_state["yapim_yili"])
    coord_submit = st.button("Kaydet")

    ########################################

    if coord_submit:
        if 1 <= int(kat_adedi) <= 5 and 1800<= int(yapim_yili)<= 2022: 
            st.session_state["kat_adedi"] = int(kat_adedi)
            st.session_state["yapim_yili"] = int(yapim_yili)
            st.success("Kaydedildi.")
            
            # İlerleme barını güncelle
            progress_bar.progress(prg_percent+10)

        else:
            st.error("Yığma bina için geçerli kat adedi veya yapım yılı giriniz.")

    ########################################
    st.subheader("Bina Fotoğrafı")
    st.write("Binanın ön cephesinden ve binayı temsil edebilecek net bir fotoğraf ekleyiniz.")
    col1, col2 = st.columns(2)
    with col1:
        st.set_option('deprecation.showfileUploaderEncoding', False)

        buffer = st.file_uploader("Fotoğraf seçin (.jpg)", type="jpg")
        temp_file = NamedTemporaryFile(delete=False)
        #st.write(temp_file)

    with col2:
        if buffer:
            temp_file.write(buffer.getvalue())
            bina_fotograf = Image.open(temp_file.name)
            st.session_state["bina_fotograf"] = bina_fotograf
            st.image(bina_fotograf)


    ########################################





elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")
import streamlit as st
from PIL import Image

st.title("Serbest Kat Adedi")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum
    #st.write("Betonarme bina tipi seçildi.")

    st.subheader("Açıklama")
    st.write("Bu yöntem 1 ila 7 katlı betonarme binalar ve 1 ila 5 katlı yığma binalar için kullanılabilir.  \
             Serbest kat adedi aşağıdaki görsel dikkate alınarak tespit edilecektir.")

    image = Image.open("./figures/kat_adedi_betonarme.jpg")
    st.image(image, width = 360)

    if "kat_adedi" not in st.session_state:
        st.session_state["kat_adedi"] = ""

    kat_adedi = st.text_input("Serbest kat adedini giriniz.", st.session_state["kat_adedi"])
    coord_submit = st.button("Kaydet")

    if coord_submit:
        if 1 <= int(kat_adedi) <= 7: 
            st.session_state["kat_adedi"] = int(kat_adedi)
            st.write("Kaydedildi")
        else:
            st.write("Betonarme bina için geçerli kat adedi giriniz.")


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")
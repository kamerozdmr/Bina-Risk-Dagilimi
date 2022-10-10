import streamlit as st
from PIL import Image

st.title("Yapısal Sistem Tipi")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum
    #st.write("Betonarme bina tipi seçildi.")

    st.subheader("Açıklama")
    st.write("Binanın taşıyıcı sistemi belirlenerek, betonarme çerçeve (BAÇ) ile \
            betonarme çerçeve ve perde (BAÇP) sistemlerinden biri olarak seçilecektir. Bodrum varsa\
            bodrum kat içinden, dükkân varsa dükkân içinden tespit edilmesi uygun olacaktır. Tespit\
            edilemiyor ise BAÇ seçilmesi uygun olacaktır."
            )

    image = Image.open("./figures/sistem_turu_gorsel.jpg")
    st.image(image, width = 720)

    sistem_tipi = st.radio(
        "Yapısal sistem tipini seçiniz.",
        ("Betonarme çerçeve (BAÇ)", "Betonarme çerçeve ve perde (BAÇP)"))

    st.session_state["sistem_tipi"] = sistem_tipi


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")

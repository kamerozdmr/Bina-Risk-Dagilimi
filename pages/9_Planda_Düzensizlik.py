import streamlit as st
from PIL import Image

st.title("Planda Düzensizlik/Burulma Etkisi")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.subheader("Açıklama")
    st.write("Planın geometrik olarak simetrik olmaması ve düşey\
            yapısal elemanların düzensiz yerleştirilmesi olarak tanımlanır. Binada burulmaya yol \
            açabilecek şekildeki plan düzensizlikleri dikkate alınacaktır."
            )

    image = Image.open("./figures/planda_duzensizlik.jpg")
    st.image(image, width = 640)

    planda_duzensizlik = st.radio(
        "Binada planında düzensizlik var mı?",
        ("Yok", "Var"))

    st.session_state["planda_duzensizlik"] = planda_duzensizlik


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.") 
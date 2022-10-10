import streamlit as st

st.title("Bina Görsel Kalitesi")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.subheader("Açıklama")
    st.write("Binanın görünen kalitesi malzeme ve işçilik kalitesine ve binanın bakımına \
            verilen önemi yansıtır. Binanın görünen kalitesi iyi(0), orta(1) ve kötü(2) olarak sınıflandırılacaktır. "
            )

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


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")
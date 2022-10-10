import streamlit as st

st.title("Deprem Tehlike Bölgesi")

st.subheader("Açıklama")
st.write("Deprem Tehlike Bölgesi, belirtilen deprem yer hareketi düzeyleri ve zemin sınıfları ile uyumlu olarak \
        esaslarda anlatıldığı şekilde dikkate alınacaktır. Yöntemde DD-2 deprem yer hareketi \
        düzeyi kullanılacak ve kısa periyot tasarım spektral ivme katsayısı (Sds) parametre değeri yürürlükte olan Türkiye Deprem Tehlike \
        Haritasından alınacaktır. Parametre değeri ile zemin sınıfları arasındaki ilişki kullanılarak \
        deprem tehlike bölgeleri belirlenecektir.")

if "ivme_katsayisi" not in st.session_state:
    st.session_state["ivme_katsayisi"] = 1.0

if "zemin_sinifi" not in st.session_state:
    st.session_state["zemin_sinifi"] = "ZA"

ivme_katsayisi = float(st.text_input("Kısa periyot tasarım spektral ivme katsayısını (Sds) giriniz.", st.session_state["ivme_katsayisi"]))

zemin_sinifi = str(st.radio(
        "Zemin sınıfını seçiniz.",
        ("ZA", "ZB", "ZC", "ZD", "ZE")))

coord_submit = st.button("Kaydet")

if coord_submit:
    st.session_state["ivme_katsayisi"] = ivme_katsayisi
    st.session_state["zemin_sinifi"] = zemin_sinifi
    st.write(f"Kaydedildi\n\nSds : {ivme_katsayisi}\n\nZemin Sınıfı : {zemin_sinifi}")

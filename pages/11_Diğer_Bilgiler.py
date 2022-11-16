import streamlit as st

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

# İlerlemeyi gösteren bar ekle
prg_percent = 90 # İlerleme yüzdesi
progress_bar = st.progress(prg_percent)

# Yan bar bilgi mesajı
st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

st.title("Diğer Bilgiler")
st.write("Verilen parametreler dışında bina hakkında girmek istediğiniz bilgileri aşağıdaki alana yazabilrisiniz.")



if "diger_bilgiler" not in st.session_state:
    st.session_state["diger_bilgiler"] = ""


diger_bilgiler = str(st.text_area(st.session_state["diger_bilgiler"], height=200))
coord_submit = st.button("Kaydet")

if coord_submit:
    st.session_state["diger_bilgiler"] = diger_bilgiler
    st.success("Kaydedildi.")

# İlerleme barını güncelle
progress_bar.progress(prg_percent+10)

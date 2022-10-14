import streamlit as st
from PIL import Image

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)

# İlerlemeyi gösteren bar ekle
prg_percent = 70 # İlerleme yüzdesi
progress_bar = st.progress(prg_percent)

# Yan bar bilgi mesajı
st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")



if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.title("Planda Düzensizlik/Burulma Etkisi")
    st.write("Planın geometrik olarak simetrik olmaması ve düşey\
            yapısal elemanların düzensiz yerleştirilmesi olarak tanımlanır. Binada burulmaya yol \
            açabilecek şekildeki plan düzensizlikleri dikkate alınacaktır."
            )

    image = Image.open("./figures/planda_duzensizlik.jpg")
    st.image(image)

    planda_duzensizlik = st.radio(
        "Binada planında düzensizlik var mı?",
        ("Yok", "Var"))

    st.session_state["planda_duzensizlik"] = planda_duzensizlik

    # İlerleme barını güncelle
    progress_bar.progress(prg_percent+10)


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum

    st.title("Planda Düzensizlik")

    st.write("Planın geometrik olarak simetrik olmaması ve düşey\
            yapısal elemanların düzensiz yerleştirilmesi olarak tanımlanır. Binada burulmaya yol \
            açabilecek şekildeki plan düzensizlikleri dikkate alınacaktır."
            )

    image = Image.open("./figures/planda_duzensizlik_durumu_yigma.jpg")
    st.image(image)


    if "planda_duzensizlik" not in st.session_state:
        st.session_state["planda_duzensizlik"] = ""
        
    planda_duzensizlik = st.slider("Bina planındaki düzensizlik seviyesini seçiniz.", 0, 2, 0)
    st.session_state["planda_duzensizlik"] = int(planda_duzensizlik)

    if st.session_state["planda_duzensizlik"] == 0:
        st.markdown("Bina planındaki düzensizlik seviyesi **Düzenli**")
    elif st.session_state["planda_duzensizlik"] == 1:
        st.markdown("Bina planındaki düzensizlik seviyesi **Az Düzenli**")
    elif st.session_state["planda_duzensizlik"] == 2:
        st.markdown("Bina planındaki düzensizlik seviyesi **Düzensiz**")


    st.write("---")
    ########################################

    st.subheader("Yatay Hatıl Yetersizliği")
    st.write("Binada yatay hatıl yetersizliği değerlendirmesinde; yatay hatıl mevcudiyeti Duvar Üstü \
            veya Pencere Üstü ise yetersizlik Yok, yok ise Var değerini alacaktır."
            )

    image = Image.open("./figures/yatay_hatil.jpg")
    st.image(image)

    yatay_hatil = st.radio(
        "Yatay hatıl yetersizliği var mı?",
        ("Yok", "Var"))

    st.session_state["yatay_hatil"] = yatay_hatil

    st.write("---")
    ########################################
    
    st.subheader("Duvar Miktarı Yetersizliği(DM)")
    st.write("Yığma binanın giriş katında yığma duvar miktarı değerlendirmesi \
            İyi, Orta ve Az için bunlara karşılık gelen olumsuzluk parametre değerleri sırasıyla 0, 1 ve 2 \
            alınacaktır."
            )

    image = Image.open("./figures/duvar_miktari.jpg")
    st.image(image)

    if "duvar_miktari" not in st.session_state:
        st.session_state["duvar_miktari"] = ""

    duvar_miktari = st.slider("Yığma duvar miktarını yukarıdaki formüle göre seçiniz.", 0, 2, 0)
    st.session_state["duvar_miktari"] = int(duvar_miktari)

    if st.session_state["duvar_miktari"] == 0:
        st.markdown("Duvar miktarı **İYİ**")
    elif st.session_state["duvar_miktari"] == 1:
        st.markdown("Duvar miktarı **ORTA**")
    elif st.session_state["duvar_miktari"] == 2:
        st.markdown("Duvar miktarı **KÖTÜ**")



    # İlerleme barını güncelle
    progress_bar.progress(prg_percent+10)

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.") 
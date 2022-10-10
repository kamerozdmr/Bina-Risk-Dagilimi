import streamlit as st
from PIL import Image

st.title("Düşeyde Düzensizlikler")

if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    st.subheader("Düşeyde Düzensizlik Durumu")
    st.write("Düşeyde devam etmeyen çerçeve ve değişen kat alanlarının etkisini \
            yansıtmak amacıyla dikkate alınacaktır. Bina yüksekliği boyunca devam etmeyen kolonlar \
            veya perdeler düşeyde düzensizlik oluşturur."
            )

    image = Image.open("./figures/duseyde_duzensizlik_gorsel.jpg")
    st.image(image, width = 720)

    duseyde_duzensizlik = st.radio(
        "Binada düşeyde düzensizlik durumunu var mı?",
        ("Yok", "Var"))

    st.session_state["duseyde_duzensizlik"] = duseyde_duzensizlik





    st.subheader("Yumuşak/Zayıf Kat Durumu")
    st.write("Kat yüksekliği farkının yanı sıra katlar arası belirgin rijitlik farkı da \
            dikkate alınarak gözlemsel olarak belirlenecektir."
            )

    image = Image.open("./figures/zayif_kat.jpg")
    st.image(image, width = 720)

    yumusak_kat = st.radio(
        "Binada yumuşak/zayıf kat durumu var mı?",
        ("Yok", "Var"))

    st.session_state["yumusak_kat"] = yumusak_kat
 




    st.subheader("Ağır Çıkma Durumu")
    st.write("Zemine oturan kat alanı ile zemin üstündeki kat alanı arasındaki farklılık belirlenecektir."
            )

    image = Image.open("./figures/agir_cikma.jpg")
    st.image(image, width = 720)

    agir_cikma = st.radio(
        "Binada ağır çıkma var mı?",
        ("Yok", "Var"))

    st.session_state["agir_cikma"] = agir_cikma
 




    st.subheader("Kısa Kolon Etkisi")
    st.write("Bu aşamada sadece dışarıdan gözlenen kısa kolonlar değerlendirmede dikkate alınacaktır."
            )

    image = Image.open("./figures/kisa_kolon.jpg")
    st.image(image, width = 280)

    kisa_kolon = st.radio(
        "Binada kısa kolon etkisi var mı?",
        ("Yok", "Var"))

    st.session_state["kisa_kolon"] = kisa_kolon




    st.subheader("Tabii Zemin Eğimi")
    st.write("Belli bir eğimin üzerindeki yamaçlarda inşa edilmiş binalarda bu etki \
            dikkate alınacaktır. Tabii zemin eğimi 30º nin altında ise tepe yamaç etkisi olmadığı, tabii zemin \
            eğimi 30º nin üzerinde ise tepe yamaç etkisi olduğu kabul edilecektir."
            )

    zemin_egimi = st.radio(
        "Zemin eğimi etkisi var mı?",
        ("Yok", "Var"))

    st.session_state["zemin_egimi"] = zemin_egimi



elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")
""" 
06.10.2022
"""

import streamlit as st

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)


st.title("Ana Sayfa")
st.subheader("Açıklama")

# Yan bar bilgi mesajı
st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")

st.write("Riskli Binanın tespiti için uygulanacak değerlendirme kuralları aşağıdaki esaslarda verilmiştir.")

st.write("[RİSKLİ YAPILARIN TESPİT EDİLMESİNE İLİŞKİN ESASLAR](https://webdosya.csb.gov.tr/db/altyapi/icerikler/r-skl--yapilarin-tesp-t-ed-lmes-ne-il-sk-n-esaslar-20190218134628.pdf)")

st.write("Bu Esaslar, 16/5/2012 tarihli 6306 sayılı Afet Riski Altındaki Alanların Dönüştürülmesi Hakkında Kanun kapsamında \
        Riskli Binaların tespit edilmesinde kullanılacak kuralları içerir. Belirli alanlarda riskli olabilecek binaların bölgesel \
        dağılımının belirlenmesi ve önceliklendirme kararı verilmesi amacıyla kullanılabilecek, bina özelliklerini ve deprem \
        tehlikesini dikkate alan basitleştirilmiş yöntemler EK-A’da verilmiştir. \n\nUygulama ile taşıyıcı sistemi betonarme ve yığma  \
        olan binaların risk tespiti bu Esaslara göre yapılmaktadır."
        )

if "bina_tipi" not in st.session_state:
    st.session_state["bina_tipi"] = "Bina tipi seçilmedi"


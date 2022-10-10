""" 
06.10.2022
"""

import streamlit as st

st.set_page_config(
    page_title = "Binaların Bölgesel Deprem Risk Dağılımını Belirlemek için Kullanılabilecek Basitleştirilmiş Yöntemler",
    #page_icon = "*"
)

if "bina_tipi" not in st.session_state:
    st.session_state["bina_tipi"] = "Bina tipi seçilmedi"

st.title("Giriş Sayfası")
st.subheader("Açıklama")
st.write("Riskli Binanın tespiti için uygulanacak değerlendirme kuralları aşağıdaki esaslarda verilmiştir. \
        \n\nhttps://webdosya.csb.gov.tr/db/altyapi/icerikler/r-skl--yapilarin-tesp-t-ed-lmes-ne-il-sk-n-esaslar-20190218134628.pdf \
        \n\nBu Esaslar, 16/5/2012 tarihli 6306 sayılı Afet Riski Altındaki Alanların Dönüştürülmesi Hakkında Kanun kapsamında \
        Riskli Binaların tespit edilmesinde kullanılacak kuralları içerir. Belirli alanlarda riskli olabilecek binaların bölgesel \
        dağılımının belirlenmesi ve önceliklendirme kararı verilmesi amacıyla kullanılabilecek, bina özelliklerini ve deprem \
        tehlikesini dikkate alan basitleştirilmiş yöntemler EK-A’da verilmiştir. \n\nUygulama ile taşıyıcı sistemi betonarme ve yığma  \
        olan binaların risk tespiti bu Esaslara göre yapılmaktadır."
        )

st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")


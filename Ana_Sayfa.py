""" 
06.10.2022
author : kamerozdmr
mail : kamer.oz@outlook.com
"""

import streamlit as st
import streamlit_authenticator as stauth
import yaml

st.set_page_config(page_title="Bina Risk Dağılımı", page_icon="figures/logo.png")

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)



# --- Authenticator ---
with open('auth/config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Giriş Ekranı', 'main')

st.session_state["authentication_status"] = authentication_status

if authentication_status == False:
        st.error("Kullanıcı adı veya parola hatalı")

if authentication_status == None:
        st.warning("Devam etmek için giriş yapınız")

if authentication_status:
        
        # --- Ana sayfa --- 
        st.title("Ana Sayfa")
        st.subheader("Açıklama")

        # Yan bar bilgi mesajı
        st.sidebar.success("Yukarıdaki değerlendirme yöntemlerini sıra ile doldurunuz.")
        authenticator.logout("Çıkış Yap", "sidebar")
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



import streamlit as st
import pandas as pd
from PIL import Image
import time  

import sys
sys.path.append("../")
from sql.insert_to_database import ConnectDatabase, InsertBetonarme, InsertYigma, InsertData, DeleteRow, EndConnection

st.set_page_config(page_title="Bina Risk Dağılımı", page_icon="figures/logo.png")

# Streamlit ana menüsünü ve footerı sayfadan kaldır
st.markdown(""" <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """, unsafe_allow_html=True)


# auth kontrol et 
if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None

if st.session_state["authentication_status"] == False:
    st.warning("Devam etmek için Ana Sayfaya dönüp giriş yapınız.")
    # Yan bar bilgi mesajı
    st.sidebar.warning("Giriş yapılmadı")

if st.session_state["authentication_status"] == None:
    st.warning("Devam etmek için Ana Sayfaya dönüp giriş yapınız.")
    # Yan bar bilgi mesajı
    st.sidebar.warning("Giriş yapılmadı")




if st.session_state["authentication_status"]:

    # Kayıt butonu Raise error
    if "sds_ss" not in st.session_state:
        st.error("Sds değeri kaydedilemedi.", icon="🚨")
        st.stop()
    else:
        if st.session_state["sds_ss"] == "clicked":
            pass
        elif st.session_state["sds_ss"] == "error":
            st.error("Sds değeri hatalı, kaydedilemedi.", icon="🚨")
            st.stop()

    # İlerlemeyi gösteren bar ekle
    prg_percent = 100 # İlerleme yüzdesi
    progress_bar = st.progress(prg_percent)

    # Ortak Fonksiyonlar
    def SliderDegeri(deger):
        if deger == 0:
            deger = "İyi" 
        elif deger == 1:
            deger = "Orta"
        elif deger == 2:
            deger = "Kötü"
        return deger

    def SliderDegeriDuzen(deger):
        if deger == 0:
            deger = "Düzenli" 
        elif deger == 1:
            deger = "Az Düzenli"
        elif deger == 2:
            deger = "Düzensiz"
        return deger

    def TehlikeBolgesiniBul(sds, zemin_sinifi):
        # Sds ve zemin sınıfına bağlı deprem tehlike bölgesini (DTB) tespit et
            
        if sds >= 1.0:
            if zemin_sinifi == "ZC" or zemin_sinifi == "ZD" or zemin_sinifi == "ZE":
                DTB = 1
            elif zemin_sinifi == "ZA" or zemin_sinifi == "ZB":
                DTB = 2
        elif 0.75 <= sds < 1.0:
            if zemin_sinifi == "ZC" or zemin_sinifi == "ZD" or zemin_sinifi == "ZE":
                DTB = 2
            elif zemin_sinifi == "ZA" or zemin_sinifi == "ZB":
                DTB = 3
        elif 0.5 <= sds < 0.75:
            if zemin_sinifi == "ZC" or zemin_sinifi == "ZD" or zemin_sinifi == "ZE":
                DTB = 3
            elif zemin_sinifi == "ZA" or zemin_sinifi == "ZB":
                DTB = 4            
        elif sds < 0.5:
            DTB = 4

        return DTB



    try:
        if st.session_state["bina_tipi"] == "Betonarme":
            #Betonarme bina tipinin seçildiği durum

            #Betonarme bina için önceki aşamalarda session state ile tanımlanmış değişkenler
            enlem = st.session_state["enlem"]
            boylam = st.session_state["boylam"]
            adres = st.session_state["adres"]
            bina_tipi = st.session_state["bina_tipi"]
            sistem_tipi = st.session_state["sistem_tipi"]
            kat_adedi = st.session_state["kat_adedi"]
            yapim_yili = st.session_state["yapim_yili"]
            yapi_no = st.session_state["yapi_no"]

            bina_fotograf = st.session_state["bina_fotograf"]
            ivme_katsayisi = st.session_state["ivme_katsayisi"]
            zemin_sinifi = st.session_state["zemin_sinifi"]

            gorsel_kalite = st.session_state["gorsel_kalite"]

            duseyde_duzensizlik = st.session_state["duseyde_duzensizlik"]
            yumusak_kat = st.session_state["yumusak_kat"]
            agir_cikma = st.session_state["agir_cikma"]
            kisa_kolon = st.session_state["kisa_kolon"] 
            zemin_egimi = st.session_state["zemin_egimi"]

            planda_duzensizlik = st.session_state["planda_duzensizlik"]

            nizam_durumu = st.session_state["nizam_durumu"]
            nizam_konumu = st.session_state["nizam_konumu"]
            doseme_seviyesi = st.session_state["doseme_seviyesi"]

            diger_bilgiler = st.session_state["diger_bilgiler"]

            def BetonarmeTabanPuanHesapla(DTB, kat_adedi):
                # Binanın kat adedi ve tehlike bölgesine göre taban puanını (TP) hesapla 

                if kat_adedi == 1 or kat_adedi == 2:
                    if DTB == 1:
                        TP = 90
                    elif DTB == 2:
                        TP = 120
                    elif DTB == 3:
                        TP = 160
                    elif DTB == 4:
                        TP = 195

                elif kat_adedi == 3:
                    if DTB == 1:
                        TP = 80
                    elif DTB == 2:
                        TP = 100
                    elif DTB == 3:
                        TP = 140
                    elif DTB == 4:
                        TP = 170

                elif kat_adedi == 4:
                    if DTB == 1:
                        TP = 70
                    elif DTB == 2:
                        TP = 90
                    elif DTB == 3:
                        TP = 130
                    elif DTB == 4:
                        TP = 160

                elif kat_adedi == 5:
                    if DTB == 1:
                        TP = 60
                    elif DTB == 2:
                        TP = 80
                    elif DTB == 3:
                        TP = 110
                    elif DTB == 4:
                        TP = 135

                elif kat_adedi == 6 or kat_adedi == 7:
                    if DTB == 1:
                        TP = 50
                    elif DTB == 2:
                        TP = 65
                    elif DTB == 3:
                        TP = 90
                    elif DTB == 4:
                        TP = 110
                
                return TP


            def BetonarmeYapısalSistemPuanıHesapla(sistem_tipi, kat_adedi):
                # Yapısal sistem tipi ve binanın kat adedine göre yapısal sistem puanı (YSP) hesapla 

                if sistem_tipi == "Betonarme çerçeve (BAÇ)":
                    YSP = 0

                elif sistem_tipi == "Betonarme çerçeve ve perde (BAÇP)":
                    if kat_adedi == 1 or kat_adedi == 2:
                        YSP = 100
                    elif kat_adedi == 3:
                        YSP = 85
                    elif kat_adedi == 4:
                        YSP = 75
                    elif kat_adedi == 5:
                        YSP = 65
                    elif kat_adedi == 6 or kat_adedi == 7:
                        YSP = 55

                return YSP



            def BetonarmeOlumsuzlukParametrePuanlarınıHesapla(kat_adedi, gorsel_kalite, duseyde_duzensizlik,yumusak_kat, agir_cikma, kisa_kolon, 
                                                            zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi):
                """ 
                Girdiler : Kat adedi, bina görsel kalitesi, düşeyde düzensizlik, yumuşak kat, ağır çıkma, kısa kolon,
                        zemin etkisi, planda düzensizlik, nizam durumu, bitişik yapının konumu, döşeme seviyesi
                Çıktı : Sıra ile olumsuzluk parametre puanlarını içeren liste
                """

                # Görsel kalite puanı (P1)
                if gorsel_kalite == 0:
                    P1 = gorsel_kalite
                elif gorsel_kalite == 1:
                    katsayi = gorsel_kalite
                    if kat_adedi == 1 or kat_adedi == 2 or  kat_adedi ==3:
                        P1 = -10 * katsayi
                    elif kat_adedi == 4:
                        P1 = -15 * katsayi
                    elif kat_adedi == 5:
                        P1 = -20 * katsayi
                    elif kat_adedi == 6 or kat_adedi == 7:
                        P1 = -25 * katsayi

                elif gorsel_kalite == 2:
                    katsayi = gorsel_kalite
                    if kat_adedi == 1 or kat_adedi == 2 or kat_adedi == 3:
                        P1 = -10 * katsayi
                    elif kat_adedi == 4:
                        P1 = -15 * katsayi
                    elif kat_adedi == 5:
                        P1 = -20 * katsayi
                    elif kat_adedi == 6 or kat_adedi == 7:
                        P1 = -25 * katsayi


                # Düşeyde düzensizlik Puanı (P2)
                if duseyde_duzensizlik == "Yok":
                    P2 = 0
                elif duseyde_duzensizlik == "Var":
                    if kat_adedi == 1 or kat_adedi == 2:
                        P2 = -5
                    elif kat_adedi == 3:
                        P2 = -10
                    elif kat_adedi == 4 or kat_adedi == 5 or kat_adedi == 6 or kat_adedi == 7:
                        P2 = -15 


                # Yumuşak kat puanı (P3)
                if yumusak_kat == "Yok":
                    P3 = 0
                elif yumusak_kat == "Var":
                    if kat_adedi == 1 or kat_adedi == 2:
                        P3 = -10
                    elif kat_adedi == 3:
                        P3 = -20
                    elif kat_adedi == 4 or kat_adedi == 5 or kat_adedi == 6 or kat_adedi == 7:
                        P3 = -30 


                # Ağır çıkma puanı (P4)
                if agir_cikma == "Yok":
                    P4 = 0
                elif agir_cikma == "Var":
                    if kat_adedi == 1 or kat_adedi == 2:
                        P4 = -10
                    elif kat_adedi == 3:
                        P4 = -20
                    elif kat_adedi == 4 or kat_adedi == 5 or kat_adedi == 6 or kat_adedi == 7:
                        P4 = -30 


                # Kısa kolon puanı (P5)
                if kisa_kolon == "Yok":
                    P5 = 0
                elif kisa_kolon == "Var":
                    P5 = -5


                # Zemin etkisi puanı (P6)
                if zemin_egimi == "Yok":
                    P6 = 0
                elif zemin_egimi == "Var":
                    P6 = -3


                # Planda düzensizlik puanı (P7)
                if planda_duzensizlik == "Yok":
                    P7 = 0
                elif planda_duzensizlik == "Var":
                    if kat_adedi == 1 or kat_adedi == 2:
                        P7 = -5
                    else:
                        P7 = -10


                # Nizam durumu puanı (P8)
                if nizam_durumu == "Ayrık":
                    P8 = 0

                elif nizam_durumu == "Bitişik":
                    if doseme_seviyesi == "Aynı":
                        if nizam_konumu == "Ortada":
                            P8 = 0
                        elif nizam_konumu == "Köşede":
                            P8 = -10

                    elif doseme_seviyesi == "Farklı":
                        if nizam_konumu == "Ortada":
                            P8 = -5
                        elif nizam_konumu == "Köşede":
                            P8 = -15

                PP_liste = [P1, P2, P3, P4, P5, P6, P7, P8]
                
                return PP_liste

            DTB = TehlikeBolgesiniBul(ivme_katsayisi, zemin_sinifi)
            TP = BetonarmeTabanPuanHesapla(DTB, kat_adedi)
            YSP = BetonarmeYapısalSistemPuanıHesapla(sistem_tipi, kat_adedi)
            OP = BetonarmeOlumsuzlukParametrePuanlarınıHesapla(kat_adedi, gorsel_kalite, duseyde_duzensizlik,yumusak_kat, agir_cikma, kisa_kolon, 
                                                            zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi )
            OP_sum = sum(OP)

            def PerformansPuanı(TP, YSP, OP):
                """ 
                Girdiler : Taban puanı (TP), yapısal sistem puanı (YSP), olumsuzluk parametre puanı (OP)
                Çıktı : A2.1'de verilen fdenkleme göre performans puanı (PP)
                """
                PP = TP + YSP + sum(OP)

                return PP

            PP = PerformansPuanı(TP, YSP, OP)
            st.header("Sonuç")
            ########################################

            col1, col2 = st.columns(2)
            with col1:
                
                st.subheader(f"Performans Puanı : {PP}")
                st.write(f"Taban Puanı : {TP}")
                st.write(f"Yapısal Sistem Puanı : {YSP}")
                st.write(f"Olumsuzluk Puanları Toplamı : {OP_sum}")
                st.write("---")
                st.write("Parametrelerin doğruluğunu kontrol ediniz ve sayfanın en altındaki butonu kullanarak veritabanına kaydediniz.")

            with col2:
                # st.subheader("Binanın Görseli")
                if bina_fotograf == "":
                    image = Image.open("./figures/fotograf_yukenmedi.jpg")
                    st.image(image)
                else:
                    st.image(bina_fotograf) 

            st.write("---")
            ########################################


            # Coğrafi koordinatları haritada göster
            st.subheader("Binanın Lokasyonu")
            coord_df = pd.DataFrame(None)
            if st.session_state["enlem"] and st.session_state["boylam"] != "":
                coord = {"lat": [st.session_state["enlem"]], "lon": [st.session_state["boylam"]]}
                coord_df = pd.DataFrame(coord)
                st.map(coord_df, zoom=12)  


            st.write("---")
            ########################################
            
            zaman =  int(time.time()) 
            st.subheader("Kaydedilen Parametreler")
            parametre_liste = ("Bina Tipi", "Sistem Tipi", "Enlem", "Boylam", "Adres Bilgisi", "Spektral ivme katsayısını (Sds)", "Zemin Sınıfı","Kat Adedi", "Yapım Yılı", "Yapı No", "Görsel Kalite", "Düşeyde Düzensizlik", "Yumuşak/Zayıf Kat", "Ağır Çıkma", "Kısa Kolon", "Zemin Eğimi", 
                            "Planda Düzensizlik", "Nizam Durumu", "Bitişik Yapı Konumu", "Bitişik Yapı Döşeme Seviyesi", "Diğer Bilgiler", "Performans Puanı", "Taban Puanı", "Yapısal Sistem Puunı", "Olumsuzluk Puanı", "Epoch Zamanı")
            parametre_tespit_liste = (bina_tipi, sistem_tipi, enlem, boylam, adres, ivme_katsayisi, zemin_sinifi, kat_adedi, yapim_yili, yapi_no, SliderDegeri(gorsel_kalite), duseyde_duzensizlik,
                                    yumusak_kat, agir_cikma, kisa_kolon, zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi,diger_bilgiler, PP, TP, YSP, OP_sum, zaman)
            

            parametre_df = pd.DataFrame({"Parametreler":parametre_liste, "Parametre Değerleri":parametre_tespit_liste})
            parametre_df = parametre_df.set_index("Parametreler")
            st.dataframe(parametre_df, width = 720, height = 920)       

            ########################################
            st.write("Parametreleri ve sonuçları kontrol ediniz ve veritabanına kaydediniz.")
            placeholder = st.empty()
            data_submit = placeholder.button("Kaydet", disabled=False)
            if data_submit:
                InsertData(parametre_tespit_liste)
                EndConnection()
                placeholder.empty()
                st.success("Veritabanına kaydedildi. \n\nYeni bina bilgisi girmek için Ana Sayfaya dönüp sayfayı yenileyin.")



        elif  st.session_state["bina_tipi"] == "Yığma":
            
            #Diğer durum olan yığma bina tipinin seçildiği durum
            
            #Betonarme bina için önceki aşamalarda session state ile tanımlanmış değişkenler
            enlem = st.session_state["enlem"]
            boylam = st.session_state["boylam"]
            adres = st.session_state["adres"]

            bina_tipi = st.session_state["bina_tipi"]

            sistem_tipi = st.session_state["sistem_tipi"]

            kat_adedi = st.session_state["kat_adedi"]
            yapim_yili = st.session_state["yapim_yili"]
            yapi_no = st.session_state["yapi_no"]
            bina_fotograf = st.session_state["bina_fotograf"]

            ivme_katsayisi = st.session_state["ivme_katsayisi"]
            zemin_sinifi = st.session_state["zemin_sinifi"]

            malzeme_kalite = st.session_state["malzeme_kalite"]
            duvar_isciligi = st.session_state["duvar_isciligi"]
            bina_hasari = st.session_state["bina_hasari"]
            cati_malzemesi = st.session_state["cati_malzemesi"]
            
            dusey_bosluk_duzensizligi = st.session_state["dusey_bosluk_duzensizligi"]
            cephe_kat_farkliligi = st.session_state["cephe_kat_farkliligi"]
            yumusak_kat = st.session_state["yumusak_kat"]
            duv_duv_baglanti = st.session_state["duv_duv_baglanti"]
            duv_dos_baglanti = st.session_state["duv_dos_baglanti"]
            doseme_tipi = st.session_state["doseme_tipi"]
            harc_malzemesi = st.session_state["harc_malzemesi"]

            planda_duzensizlik = st.session_state["planda_duzensizlik"]
            yatay_hatil = st.session_state["yatay_hatil"]
            duvar_miktari = st.session_state["duvar_miktari"]

            nizam_durumu = st.session_state["nizam_durumu"]
            nizam_konumu = st.session_state["nizam_konumu"]
            doseme_seviyesi = st.session_state["doseme_seviyesi"]

            diger_bilgiler = st.session_state["diger_bilgiler"]
            
            
            def YigmaTabanPuanHesapla(DTB, kat_adedi):
                # Binanın kat adedi ve tehlike bölgesine göre taban puanını (TP) hesapla 
                
                if kat_adedi == 1:
                    if DTB == 1:
                        TP = 110
                    elif DTB == 2 or kat_adedi == 3:
                        TP = 120
                    elif DTB == 4:
                        TP = 130

                
                elif kat_adedi == 2:
                    if DTB == 1:
                        TP = 100
                    elif DTB == 2 or kat_adedi == 3:
                        TP = 110
                    elif DTB == 4:
                        TP = 120

                elif kat_adedi == 3:
                    if DTB == 1:
                        TP = 90
                    elif DTB == 2 or kat_adedi == 3:
                        TP = 100
                    elif DTB == 4:
                        TP = 110

                elif kat_adedi == 4:
                    if DTB == 1:
                        TP = 80
                    elif DTB == 2 or kat_adedi == 3:
                        TP = 90
                    elif DTB == 4:
                        TP = 100

                elif kat_adedi == 5:
                    if DTB == 1:
                        TP = 70
                    elif DTB == 2 or kat_adedi == 3:
                        TP = 80
                    elif DTB == 4:
                        TP = 90

                return TP

            def YigmaYapısalSistemPuanıHesapla(sistem_tipi):
                # Yapısal sistem tipine göre yapısal sistem puanı (YSP) hesapla 

                if sistem_tipi == "Donatısız Yığma":
                    YSP = 0

                elif sistem_tipi == "Donatılı Yığma":
                    YSP = 60

                if sistem_tipi == "Kuşatılmış Yığma":
                    YSP = 30

                elif sistem_tipi == "Karma":
                    YSP = 0

                return YSP


            def YigmaOlumsuzlukParametrePuanlarınıHesapla(kat_adedi, malzeme_kalite, duvar_isciligi, bina_hasari, cati_malzemesi, dusey_bosluk_duzensizligi,
                                                                cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, harc_malzemesi,
                                                                planda_duzensizlik, yatay_hatil, duvar_miktari, nizam_durumu, nizam_konumu, doseme_seviyesi):
                """ 
                Girdiler : Kat adedi, malzeme türü ve kalitesi, duvar işçiliği, mevcut hasar durumu, çatı malzemesi, düşey boşluk düzensizliği, cepheye göre kat sayısı farkı,
                yumuşak kat, duvar-duvar bağlantısı, duvar-döşeme bağlantısı, döşeme tipi, harç malzememsi, planda düzensizlik, yatay hatıl yetersizliği, duvar miktarı
                nizam durumu, bitişik yapının konumu, döşeme seviyesi
                Çıktı : Sıra ile olumsuzluk parametre puanlarını içeren liste
                """

                # Malzeme kalite puanı (P1)
                katsayi = malzeme_kalite
                P1 = katsayi * -10
                
                # Duvar işçiliği (P2)
                katsayi = duvar_isciligi
                P2 = katsayi * -5

                # Mevcut hasat durumu (P3)
                if bina_hasari == "Yok":
                    P3 = 0
                elif bina_hasari == "Var":
                    P3 = -5
                
                # Çatı malzemesi (P4)
                if cati_malzemesi == "Kiremit, Saç veya Beton":
                    P4 = 0
                elif cati_malzemesi == "Toprak":
                    P4 = -10
                
                # Düşey boşluk düzensizliği (P5)
                katsayi = dusey_bosluk_duzensizligi
                if kat_adedi == 1:
                    P5 = 0 
                elif kat_adedi == 2 or kat_adedi == 3:
                    P5 = katsayi * -5
                elif kat_adedi == 4 or kat_adedi == 5:
                    P5 = katsayi * -10
                
                # Cepheye göre kat sayısı farkı (P6)
                if cephe_kat_farkliligi == "Yok":
                    P6 = 0
                elif cephe_kat_farkliligi == "Var":
                    P6 = -5

                # Yumuşak/Zayıf kat (P7)
                if yumusak_kat == "Yok":
                    P7 = 0
                elif yumusak_kat == "Var":
                    if kat_adedi == 1:
                        P7 = 0
                    elif kat_adedi == 2 or kat_adedi == 3:
                        P7 = -5
                    elif kat_adedi == 4 or kat_adedi == 5:
                        P7 = -10

                # Düzlem Dışı Davranış Olumsuzlukları (P8)
                sayac = 0
                if duv_duv_baglanti == "Kötü":
                    sayac += 1
                if duv_dos_baglanti == "Kötü":
                    sayac += 1
                if doseme_tipi == "Ahşap veya Volto":
                    sayac += 1
                if harc_malzemesi == "Kireç, Çamur veya Yok":
                    sayac += 1
                
                if sayac >= 3:
                    P8 = -10
                else:
                    P8 = 0

                # Planda düzensizlik (P9)
                katsayi = planda_duzensizlik
                if kat_adedi == 1:
                    P9 = katsayi * -5
                elif kat_adedi == 2 or kat_adedi == 3:
                    P9 = katsayi * -10
                elif kat_adedi == 4:
                    P9 = katsayi * -15
                elif kat_adedi == 5:
                    P9 = katsayi * -20

                # Yatay hatıl yetersizliği (P10)
                if yatay_hatil == "Yok":
                    P10 = 0
                elif yatay_hatil == "Var":
                    P10 = -5

                # Duvar miktarı (P11)
                katsayi = duvar_miktari
                if kat_adedi == 1 or kat_adedi == 2:
                    P11 = katsayi * -5
                elif kat_adedi == 3 or kat_adedi == 4:
                    P11 = katsayi * -10
                elif kat_adedi == 5:
                    P11 = katsayi * -15


                # Nizam durumu puanı (P12)
                if nizam_durumu == "Ayrık":
                    P12 = 0

                elif nizam_durumu == "Bitişik":
                    if doseme_seviyesi == "Aynı":
                        if nizam_konumu == "Ortada":
                            P12 = 0
                        elif nizam_konumu == "Köşede":
                            P12 = -5

                    elif doseme_seviyesi == "Farklı":
                        if nizam_konumu == "Ortada":
                            P12 = -5
                        elif nizam_konumu == "Köşede":
                            P12 = -10
                

                PP_liste = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12]
                
                return PP_liste



            DTB = TehlikeBolgesiniBul(ivme_katsayisi, zemin_sinifi)
            TP = YigmaTabanPuanHesapla(DTB, kat_adedi)
            YSP = YigmaYapısalSistemPuanıHesapla(sistem_tipi)


            OP = YigmaOlumsuzlukParametrePuanlarınıHesapla(kat_adedi, malzeme_kalite, duvar_isciligi, bina_hasari, cati_malzemesi, dusey_bosluk_duzensizligi,
                                                            cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, harc_malzemesi,
                                                            planda_duzensizlik, yatay_hatil, duvar_miktari, nizam_durumu, nizam_konumu, doseme_seviyesi)
            OP_sum = sum(OP)
            def PerformansPuanı(TP, YSP, OP):
                """ 
                Girdiler : Taban puanı (TP), yapısal sistem puanı (YSP), olumsuzluk parametre puanı (OP)
                Çıktı : A2.1'de verilen fdenkleme göre performans puanı (PP)
                """
                PP = TP + YSP + sum(OP)

                return PP

            PP = PerformansPuanı(TP, YSP, OP)

            st.header("Sonuç")
            ########################################

            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"Performans Puanı : {PP}")
                st.write(f"Taban Puanı : {TP}")
                st.write(f"Yapısal Sistem Puanı : {YSP}")
                st.write(f"Olumsuzluk Puanları Toplamı : {OP_sum}")
                st.write("---")
                st.write("Parametrelerin doğruluğunu kontrol ediniz ve sayfanın en altındaki butonu kullanarak veritabanına kaydediniz.")

            with col2:
                # st.subheader("Binanın Görseli")
                if bina_fotograf == "":
                    image = Image.open("./figures/fotograf_yukenmedi.jpg")
                    st.image(image)
                else:
                    st.image(bina_fotograf) 
                

            st.write("---")
            ########################################

            # Coğrafi koordinatları haritada göster
            st.subheader("Binanın Lokasyonu")
            coord_df = pd.DataFrame(None)
            if st.session_state["enlem"] and st.session_state["boylam"] != "":
                coord = {"lat": [st.session_state["enlem"]], "lon": [st.session_state["boylam"]]}
                coord_df = pd.DataFrame(coord)
                st.map(coord_df, zoom=12)  


            st.write("---")
            ########################################

            st.subheader("Kaydedilen Parametreler")
            zaman =  int(time.time()) 

            parametre_liste = ("Bina Tipi", "Sistem Tipi", "Enlem", "Boylam", "Adres Bilgisi", "Spektral ivme katsayısını (Sds)", "Zemin Sınıfı","Kat Adedi", "Yapım Yılı", "Yapı No",
                            "Malzeme Türü ve Kalitesi", "Yığma Duvar İşciliği", "Mevcut Hasar", "Çatı Malzemesi", "Düşey Boşluk Düzensizliği", "Cepheye Göre Kat Sayısı Farklılığı",
                            "Yumuşak/Zayıf Kat", "Duvar-Duvar Bağlantıları", "Duvar-Döşeme Bağlantıları", "Döşeme Tipi", "Harç Malzemesi", "Planda Düzensizlik", "Yatay Hatıl Yetersizliği",
                            "Duvar Miktarı", "Nizam Durumu", "Bitişik Yapı Konumu", "Bitişik Yapı Döşeme Seviyesi", "Diğer Bilgiler", "Performans Puanı", "Taban Puanı", "Yapısal Sistem Puunı", "Olumsuzluk Puanı", "Epoch Zamanı")

            parametre_tespit_liste = (bina_tipi, sistem_tipi, enlem, boylam, adres, ivme_katsayisi, zemin_sinifi, kat_adedi, yapim_yili, yapi_no, SliderDegeri(malzeme_kalite), SliderDegeri(duvar_isciligi),
                                    bina_hasari, cati_malzemesi, SliderDegeriDuzen(dusey_bosluk_duzensizligi), cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, 
                                    harc_malzemesi, SliderDegeriDuzen(planda_duzensizlik), yatay_hatil, SliderDegeri(duvar_miktari), nizam_durumu, nizam_konumu, doseme_seviyesi, diger_bilgiler, PP, TP, YSP, OP_sum, zaman)

            parametre_df = pd.DataFrame({"Parametreler":parametre_liste, "Parametre Değerleri":parametre_tespit_liste})
            parametre_df = parametre_df.set_index("Parametreler")
            st.dataframe(parametre_df, width = 720, height = 1150)       

            ########################################

            st.write("Parametreleri ve sonuçları kontrol ettikten sonra veritabanına kaydediniz.")
            placeholder = st.empty()
            data_submit = placeholder.button("Kaydet", disabled=False)
            if data_submit:
                InsertData(parametre_tespit_liste)
                EndConnection()
                placeholder.empty()
                st.success("Veritabanına kaydedildi. \n\nYeni bina bilgisi girmek için Ana Sayfaya dönüp sayfayı yenileyin.")


        elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
            st.write("Bina tipini seçiniz.")


    except Exception as e:
        hata_mesaji = getattr(e, "message", repr(e))
        st.error("Hata", icon="🚨")
        st.warning(f"Bilgilerin eksiksiz ve doğru formatta olduğunu kontrol ediniz.\n\nHata Mesajı : {hata_mesaji}")




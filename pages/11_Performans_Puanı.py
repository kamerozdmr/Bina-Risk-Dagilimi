import streamlit as st
import pandas as pd

st.title("Sonuç")


if st.session_state["bina_tipi"] == "Betonarme":
    #Betonarme bina tipinin seçildiği durum

    #Betonarme bina için önceki aşamalarda session state ile tanımlanmış değişkenler
    enlem = st.session_state["lat_input"]
    boylam = st.session_state["lon_input"]
    bina_tipi = st.session_state["bina_tipi"]
    sistem_tipi = st.session_state["sistem_tipi"]
    kat_adedi = st.session_state["kat_adedi"]
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


    def TehlikeBolgesiniBul(sds, zemin_sinifi):
        # Sds ve zemin sınıfına bağlı deprem tehlike bölgesini (DTB) tespit et
    
        if sds >= 1.0:
            if zemin_sinifi == "ZC" or "ZD" or "ZE":
                DTB = 1
            elif zemin_sinifi == "ZA" or "ZB":
                DTB = 2
        elif 0.75 <= sds < 1.0:
            if zemin_sinifi == "ZC" or "ZD" or "ZE":
                DTB = 2
            elif zemin_sinifi == "ZA" or "ZB":
                DTB = 3
        elif 0.5 <= sds < 0.75:
            if zemin_sinifi == "ZC" or "ZD" or "ZE":
                DTB = 3
            elif zemin_sinifi == "ZA" or "ZB":
                DTB = 4            
        elif sds < 0.5:
            DTB = 4

        return DTB


    def TabanPuanHesapla(DTB, kat_adedi):
        # Binanın kat adedi ve tehlike bölgesine göre taban puanını (TP) hesapla 

        if kat_adedi == 1 or 2:
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

        elif kat_adedi == 6 or 7:
            if DTB == 1:
                TP = 50
            elif DTB == 2:
                TP = 65
            elif DTB == 3:
                TP = 90
            elif DTB == 4:
                TP = 110
        
        return TP


    def YapısalSistemPuanıHesapla(sistem_tipi, kat_adedi):
        # Yapısal sistem tipi ve binanın kat adedine göre yapısal sistem puanı (YSP) hesapla 

        if sistem_tipi == "Betonarme çerçeve (BAÇ)":
            YSP = 0

        elif sistem_tipi == "Betonarme çerçeve ve perde (BAÇP)":
            if kat_adedi == 1 or 2:
                YSP = 100
            elif kat_adedi == 3:
                YSP = 85
            elif kat_adedi == 4:
                YSP = 75
            elif kat_adedi == 5:
                YSP = 65
            elif kat_adedi == 6 or 7:
                YSP = 55

        return YSP



    def OlumsuzlukParametrePuanlarınıHesapla(kat_adedi, gorsel_kalite, duseyde_duzensizlik,yumusak_kat, agir_cikma, kisa_kolon, 
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
            if kat_adedi == 1 or 2 or 3:
                P1 = -10 * katsayi
            elif kat_adedi == 4:
                P1 = -15 * katsayi
            elif kat_adedi == 5:
                P1 = -20 * katsayi
            elif kat_adedi == 6 or 7:
                P1 = -25 * katsayi

        elif gorsel_kalite == 2:
            katsayi = gorsel_kalite
            if kat_adedi == 1 or 2 or 3:
                P1 = -10 * katsayi
            elif kat_adedi == 4:
                P1 = -15 * katsayi
            elif kat_adedi == 5:
                P1 = -20 * katsayi
            elif kat_adedi == 6 or 7:
                P1 = -25 * katsayi


        # Düşeyde düzensizlik Puanı (P2)
        if duseyde_duzensizlik == "Yok":
            P2 = 0
        elif duseyde_duzensizlik == "Var":
            if kat_adedi == 1 or 2:
                P2 = -5
            elif kat_adedi == 3:
                P2 = -10
            elif kat_adedi == 4 or 5 or 6 or 7:
                P2 = -15 


        # Yumuşak kat puanı (P3)
        if yumusak_kat == "Yok":
            P3 = 0
        elif yumusak_kat == "Var":
            if kat_adedi == 1 or 2:
                P3 = -10
            elif kat_adedi == 3:
                P3 = -20
            elif kat_adedi == 4 or 5 or 6 or 7:
                P3 = -30 


        # Ağır çıkma puanı (P4)
        if agir_cikma == "Yok":
            P4 = 0
        elif agir_cikma == "Var":
            if kat_adedi == 1 or 2:
                P4 = -10
            elif kat_adedi == 3:
                P4 = -20
            elif kat_adedi == 4 or 5 or 6 or 7:
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
            if kat_adedi == 1 or 2:
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
    TP = TabanPuanHesapla(DTB, kat_adedi)
    YSP = YapısalSistemPuanıHesapla(sistem_tipi, kat_adedi)
    OP = OlumsuzlukParametrePuanlarınıHesapla(kat_adedi, gorsel_kalite, duseyde_duzensizlik,yumusak_kat, agir_cikma, kisa_kolon, 
                                             zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi )

    def PerformansPuanı(TP, YSP, OP):
        """ 
        Girdiler : Taban puanı (TP), yapısal sistem puanı (YSP), olumsuzluk parametre puanı (OP)
        Çıktı : A2.1'de verilen fdenkleme göre performans puanı (PP)
        """
        PP = TP + YSP + sum(OP)

        return PP

    PP = PerformansPuanı(TP, YSP, OP)


    st.subheader(f"Performans Puanı : {PP}")
    st.write(f"Taban Puanı : {TP}")
    st.write(f"Yapısal Sistem Puanı : {YSP}")
    st.write(f"Olumsuzluk Parametre Puanları Toplamı : {sum(OP)}")

    
    st.subheader("Parametreler")
    parametre_liste = ["Bina Tipi", "Sistem Tipi", "Enlem", "Boylam", "Spektral ivme katsayısını (Sds)", "Zemin Sınıfı","Kat Adedi", "Görsel Kalite", "Düşeyde Düzensizlik", "Yumuşak/Zayıf Kat", "Ağır Çıkma", "Kısa Kolon", "Zemin Eğimi", 
                       "Planda Düzensizlik", "Nizam Durumu", "Bitişik Yapı Konumu", "Bitişik Yapı Döşeme Seviyesi"]
    parametre_tespit_liste = [bina_tipi, sistem_tipi, enlem, boylam, ivme_katsayisi, zemin_sinifi, kat_adedi, gorsel_kalite, duseyde_duzensizlik,yumusak_kat, agir_cikma, kisa_kolon, 
                              zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi]
    
    parametre_df = pd.DataFrame({"Parametreler":parametre_liste, "Parametre Değerleri":parametre_tespit_liste})
    parametre_df = parametre_df.set_index("Parametreler")
    st.dataframe(parametre_df, width=480, height=640)


    # Coğrafi koordinatları haritada göster
    st.subheader("Binanın Lokasyonu")
    coord_df = pd.DataFrame(None)
    if st.session_state["lat_input"] and st.session_state["lon_input"] != "":
        d = {"lat": [st.session_state["lat_input"]], "lon": [st.session_state["lon_input"]]}
        coord_df = pd.DataFrame(d)

    st.map(coord_df, zoom=13, use_container_width=800)
    


elif  st.session_state["bina_tipi"] == "Yığma":
    #Diğer durum olan yığma bina tipinin seçildiği durum
    st.write("Yığma bina tespiti yapım aşamasında...")

elif st.session_state["bina_tipi"] == "Bina tipi seçilmedi":
    st.write("Bina tipini seçiniz.")
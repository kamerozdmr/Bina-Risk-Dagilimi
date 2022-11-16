import mysql.connector
import streamlit as st

def ConnectDatabase():
    global db
    global cursor

    db = mysql.connector.connect(**st.secrets["mysql"]
    )
    
    cursor = db.cursor()


def InsertBetonarme(data):
    ConnectDatabase()

    insert_betonarme = ("INSERT INTO betonarme "
               "(bina_tipi, sistem_tipi, enlem, boylam, adres, sds, zemin_sinifi, kat_adedi, yapim_yili, yapi_no, gorsel_kalite, duseyde_duzensizlik, \
               yumusak_kat, agir_cikma, kisa_kolon, zemin_egimi, planda_duzensizlik, nizam_durumu, nizam_konumu, doseme_seviyesi, diger_bilgiler, performans_puani, taban_puani, yapisal_sistem_puani, olumsuzluk_puani, zaman) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    #data_betonarme = (zaman, 'Betonarme', 'Betonarme çerçeve (BAÇ)', 40.559, 30.455, 'Adres Safranbolu, Karabük', 1.53, 'ZC', 6, 1995, 'İyi', 'Yok', 'Var','Yok', 'Var', 'Yok', 'Var','Bitişik', 'Ortada','Farklı','Falanda filan gev gev gev' )
    
    cursor.execute(insert_betonarme, data)
    db.commit()

    


def InsertYigma(data):
    ConnectDatabase()
    insert_yigma = ("INSERT INTO yigma "
                "(bina_tipi, sistem_tipi, enlem, boylam, adres, sds, zemin_sinifi, kat_adedi, yapim_yili, yapi_no, malzeme_kalite, duvar_isciligi, bina_hasari, \
                cati_malzemesi, dusey_bosluk_duzensizligi, cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, harc_malzemesi, \
                planda_duzensizlik, yatay_hatil, duvar_miktari, nizam_durumu, nizam_konumu, doseme_seviyesi, diger_bilgiler, performans_puani, taban_puani, yapisal_sistem_puani, olumsuzluk_puani, zaman) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    #data = (zaman, 'Yığma', 'Donatılı Yığma', 40.559, 30.455, 'Adres Safranbolu, Karabük', 1.53, 'ZC', 6, 1995, 'Orta', 'Orta', 'Var','Toprak', 'Az Düzenli', 'Yok', 'Var','Kötü', 'İyi','Ahşap veya Volto','Kireç, Çamur veya Yok','Düzenli','Yok','İyi','Bitişik','','','Falan filan falan filan' )
    
    cursor.execute(insert_yigma, data)
    db.commit()


def InsertData(data):  
    if data[0] == 'Betonarme':
        InsertBetonarme(data)
    
    elif data[0] == 'Yığma':
        InsertYigma(data)


def DeleteRow(data):
    delete_row = "DELETE FROM `yigma` WHERE `zaman` = %s;"
    cursor.execute(delete_row, data[-1])
    db.commit()


def EndConnection():
    cursor.close()
    db.close()


"""
ConnectDatabase()
insert_yigma = ("INSERT INTO yigma "
                "(bina_tipi, sistem_tipi, enlem, boylam, adres, sds, zemin_sinifi, kat_adedi, yapim_yili, malzeme_kalite, duvar_isciligi, bina_hasari, \
                cati_malzemesi, dusey_bosluk_duzensizligi, cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, harc_malzemesi, \
                planda_duzensizlik, yatay_hatil, duvar_miktari, nizam_durumu, nizam_konumu, doseme_seviyesi, diger_bilgiler, performans_puani, taban_puani, yapisal_sistem_puani, olumsuzluk_puani, zaman) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

data = ('Yığma', 'Donatılı Yığma', 40.559, 30.455, 'Adres Safranbolu, Karabük', 1.53, 'ZC', 6, 1995, 'Orta', 'Orta', 'Var','Toprak', 'Az Düzenli', 'Yok', 'Var','Kötü', 'İyi','Ahşap veya Volto','Kireç, Çamur veya Yok','Düzenli','Yok','İyi','Bitişik','','','Falan filan falan filan',10, 10, 10, 10, 111111 )
    
cursor.execute(insert_yigma, data)
db.commit()



ConnectDatabase()
global cursor
cursor = db.cursor()

insert_yigma = ("INSERT INTO yigma "
                "(bina_tipi, sistem_tipi, enlem, boylam, adres, sds, zemin_sinifi, kat_adedi, yapim_yili, malzeme_kalite, duvar_isciligi, bina_hasari, \
                cati_malzemesi, dusey_bosluk_duzensizligi, cephe_kat_farkliligi, yumusak_kat, duv_duv_baglanti, duv_dos_baglanti, doseme_tipi, harc_malzemesi, \
                planda_duzensizlik, yatay_hatil, duvar_miktari, nizam_durumu, nizam_konumu, doseme_seviyesi, diger_bilgiler, zaman) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

data = ('Yığma', 'Donatılı Yığma', 40.559, 30.455, 'Adres Safranbolu, Karabük', 1.53, 'ZC', 6, 1995, 'Orta', 'Orta', 'Var','Toprak', 'Az Düzenli', 'Yok', 'Var','Kötü', 'İyi','Ahşap veya Volto','Kireç, Çamur veya Yok','Düzenli','Yok','İyi','Bitişik','','','Falan filan falan filan', 1000 )
    
cursor.execute(insert_yigma, data)
db.commit()

#cursor.close()
#db.close()

delete_row = "DELETE FROM `yigma` WHERE `zaman` = 1000;"

cursor.execute(delete_row)
db.commit()
"""

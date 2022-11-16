import mysql.connector    # Add mysql.connector
import time    


def ConnectDatabase():
    db = mysql.connector.connect(
        host = "brszbfzivrn3j48wj4kf-mysql.services.clever-cloud.com",
        user = "usibk0lh64mtzqnv",
        passwd = "lRORSIr3CVZS0tjNNfRr",
        database = "brszbfzivrn3j48wj4kf"
    ) 

    return db

def SendtoDatabase(db):
    """
    Function Input : "Database", "Bina Tipi", "Sistem Tipi", "Enlem", "Boylam", "Adres Bilgisi", "Spektral ivme katsayısını (Sds)", "Zemin Sınıfı","Kat Adedi", "Yapım Yılı", 
            "Malzeme Türü ve Kalitesi", "Yığma Duvar İşciliği", "Mevcut Hasar", "Çatı Malzemesi", "Düşey Boşluk Düzensizliği", "Cepheye Göre Kat Sayısı Farklılığı",
            "Yumuşak/Zayıf Kat", "Duvar-Duvar Bağlantıları", "Duvar-Döşeme Bağlantıları", "Döşeme Tipi", "Harç Malzemesi", "Planda Düzensizlik", "Yatay Hatıl Yetersizliği",
            "Duvar Miktarı", "Nizam Durumu", "Bitişik Yapı Konumu", "Bitişik Yapı Döşeme Seviyesi", "Diğer Bilgiler"
    Database Input : "epoch_zamani", "bina_tipi", "sistem_tipi", "enlem", "boylam", "adres_bilgisi", "sds", "zemin_sinifi", "kat_adedi", "yapim_yili", "malzeme_turu",
                     "duvar_isciligi", "mevcut_hasar", "cati_malzemesi", "bosluk_duzensizligi, "cephe_kat_farkliligi", "yumusak_kat", "duvar_duvar_baglantisi", "duvar_doseme_baglantisi",
                     "doseme_tipi", "harc_malzemesi", "planda_duzensizlik", "yatay_hatil_yetersizligi", "duvar_miktari" 

    """
    """
    now = datetime.now()
    tarih_string = now.strftime("%d-%m-%Y")
    saat_string = now.strftime("%H:%M:%S")
    """
    epoch_zamani = int(time.time())
    # Cursor oluştur
    return  None

db = ConnectDatabase()
mycursor = db.cursor()
    # Tablo zaten varsa tablo oluşturmadan devam et
#mycursor.execute("DROP TABLE IF EXISTS yigma")                                      
    # Tabloyu oluştur
#mycursor.execute("CREATE TABLE yigma (tarih VARCHAR(255), saat VARCHAR(255))")    

sql = "INSERT IGNORE INTO yigma (tarih, saat) VALUES (%s, %s)"
val = ("nuri", "safranbolu")

mycursor.execute(sql, val)
db.commit()
    




"""
parametre_liste = [ "Tarih", "Saat", "Bina Tipi", "Sistem Tipi", "Enlem", "Boylam", "Adres Bilgisi", "Spektral ivme katsayısını (Sds)", "Zemin Sınıfı","Kat Adedi", "Yapım Yılı", 
                           "Malzeme Türü ve Kalitesi", "Yığma Duvar İşciliği", "Mevcut Hasar", "Çatı Malzemesi", "Düşey Boşluk Düzensizliği", "Cepheye Göre Kat Sayısı Farklılığı",
                           "Yumuşak/Zayıf Kat", "Duvar-Duvar Bağlantıları", "Duvar-Döşeme Bağlantıları", "Döşeme Tipi", "Harç Malzemesi", "Planda Düzensizlik", "Yatay Hatıl Yetersizliği",
                           "Duvar Miktarı", "Nizam Durumu", "Bitişik Yapı Konumu", "Bitişik Yapı Döşeme Seviyesi", "Diğer Bilgiler"]
"""


"""
# Placeholder example
ph = "%s is the best %s to learn Python"
print(ph%("Examples", "way"))
"""
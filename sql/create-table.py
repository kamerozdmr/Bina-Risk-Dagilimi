import mysql.connector
from mysql.connector import errorcode

try:
    # Connecting to MySQL Using Connector/Python
    db = mysql.connector.connect(
        host = "brszbfzivrn3j48wj4kf-mysql.services.clever-cloud.com",
        user = "usibk0lh64mtzqnv",
        passwd = "lRORSIr3CVZS0tjNNfRr",
        database = "brszbfzivrn3j48wj4kf"
        )

    print("Connected to database succesfully")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


# Table descriptions
TABLES = {}
TABLES['betonarme'] = (
    "CREATE TABLE `betonarme` ("
    "  `bina_no` INT(6) NOT NULL AUTO_INCREMENT,"
    "  `bina_tipi` ENUM('Betonarme','Yığma') NOT NULL,"
    "  `sistem_tipi` ENUM('Betonarme çerçeve (BAÇ)','Betonarme çerçeve ve perde (BAÇP)') NOT NULL,"
    "  `enlem` FLOAT(9,6) NOT NULL,"
    "  `boylam` FLOAT(9,6) NOT NULL,"
    "  `adres` VARCHAR(255) NOT NULL,"
    "  `sds` FLOAT(5,3) NOT NULL,"
    "  `zemin_sinifi` ENUM('ZA','ZB', 'ZC','ZD', 'ZE') NOT NULL,"
    "  `kat_adedi` INT(2) NOT NULL,"
    "  `yapim_yili` INT(4) NOT NULL,"
    "  `gorsel_kalite` ENUM('İyi','Orta', 'Kötü') NOT NULL,"
    "  `duseyde_duzensizlik` ENUM('Yok','Var') NOT NULL,"
    "  `yumusak_kat` ENUM('Yok','Var') NOT NULL,"
    "  `agir_cikma` ENUM('Yok','Var') NOT NULL,"
    "  `kisa_kolon` ENUM('Yok','Var') NOT NULL,"
    "  `zemin_egimi` ENUM('Yok','Var') NOT NULL,"
    "  `planda_duzensizlik` ENUM('Yok','Var') NOT NULL,"
    "  `nizam_durumu` ENUM('Ayrık','Bitişik') NOT NULL,"
    "  `nizam_konumu` ENUM('Ortada','Köşede',''),"
    "  `doseme_seviyesi` ENUM('Aynı','Farklı',''),"
    "  `diger_bilgiler` VARCHAR(255),"
    "  `performans_puani` INT(3) NOT NULL,"
    "  `taban_puani` INT(3) NOT NULL,"
    "  `yapisal_sistem_puani` INT(3) NOT NULL,"
    "  `olumsuzluk_puani` INT(3) NOT NULL,"
    "  `zaman` INT(11) NOT NULL,"
    "  PRIMARY KEY (`bina_no`)"
    ") ENGINE=InnoDB")


TABLES['yigma'] = (
    "CREATE TABLE `yigma` ("
    "  `bina_no` INT(6) NOT NULL AUTO_INCREMENT,"
    "  `bina_tipi` ENUM('Betonarme','Yığma') NOT NULL,"
    "  `sistem_tipi` ENUM('Donatısız Yığma', 'Donatılı Yığma', 'Kuşatılmış Yığma', 'Karma') NOT NULL,"
    "  `enlem` FLOAT(9,6) NOT NULL,"
    "  `boylam` FLOAT(9,6) NOT NULL,"
    "  `adres` VARCHAR(255) NOT NULL,"
    "  `sds` FLOAT(5,3) NOT NULL,"
    "  `zemin_sinifi` ENUM('ZA','ZB', 'ZC','ZD', 'ZE') NOT NULL,"
    "  `kat_adedi` INT(2) NOT NULL,"
    "  `yapim_yili` INT(4) NOT NULL,"
    "  `malzeme_kalite` ENUM('İyi','Orta', 'Kötü') NOT NULL,"
    "  `duvar_isciligi` ENUM('İyi','Orta', 'Kötü') NOT NULL,"
    "  `bina_hasari` ENUM('Yok','Var') NOT NULL,"
    "  `cati_malzemesi` ENUM('Kiremit, Saç veya Beton','Toprak') NOT NULL,"
    "  `dusey_bosluk_duzensizligi` ENUM('Düzenli','Az Düzenli', 'Düzensiz') NOT NULL,"
    "  `cephe_kat_farkliligi` ENUM('Yok','Var') NOT NULL,"
    "  `yumusak_kat` ENUM('Yok','Var') NOT NULL,"
    "  `duv_duv_baglanti` ENUM('İyi','Kötü') NOT NULL,"
    "  `duv_dos_baglanti` ENUM('İyi','Kötü') NOT NULL,"
    "  `doseme_tipi` ENUM('Betonarme','Ahşap veya Volto') NOT NULL,"
    "  `harc_malzemesi` ENUM('Çimento','Kireç, Çamur veya Yok') NOT NULL,"
    "  `planda_duzensizlik` ENUM('Düzenli','Az Düzenli', 'Düzensiz') NOT NULL,"
    "  `yatay_hatil` ENUM('Yok','Var') NOT NULL,"
    "  `duvar_miktari` ENUM('İyi','Orta', 'Kötü') NOT NULL,"
    "  `nizam_durumu` ENUM('Ayrık','Bitişik') NOT NULL,"
    "  `nizam_konumu` ENUM('Ortada','Köşede',''),"
    "  `doseme_seviyesi` ENUM('Aynı','Farklı',''),"
    "  `diger_bilgiler` VARCHAR(255),"
    "  `performans_puani` INT(3) NOT NULL,"
    "  `taban_puani` INT(3) NOT NULL,"
    "  `yapisal_sistem_puani` INT(3) NOT NULL,"
    "  `olumsuzluk_puani` INT(3) NOT NULL,"
    "  `zaman` INT(11) NOT NULL,"
    "  PRIMARY KEY (`bina_no`)"
    ") ENGINE=InnoDB")


# Create cursor
cursor = db.cursor()

# Create Tables
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cursor.close()
db.close()
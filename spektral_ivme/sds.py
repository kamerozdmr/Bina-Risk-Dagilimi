import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

def rounder(sayi):
    # Parametrelerde verilen enlem boylam değerlerine göre yuvarla
    r = round(sayi, 1) 
    if round((sayi - r),3) == 0.05 or round((sayi - r),3) == -0.05:
        a, b = round(sayi,2), round(sayi,2)
    else:
        a, b = round((r-0.05),2), round((r+0.05),2)
    return a, b



def getAccCoeff(enlem, boylam, zemin):
    df = pd.read_excel("spektral_ivme/parametreler.xlsx")

    b_low, b_high = rounder(boylam)
    e_low, e_high = rounder(enlem) 
   
    ss_array = np.empty([2,2])
    
    # Boylam değerlerinin indexleri
    b_low_ind = df[df["boylam"]==b_low].index
    b_high_ind = df[df["boylam"]==b_high].index
    # Boylam değerleri dataframeler
    b_low_df = df.iloc[b_low_ind[0]:b_low_ind[-1]]
    b_high_df = df.iloc[b_high_ind[0]:b_high_ind[-1]]
    # Enlem değeri indexi
    bl_el_ind = b_low_df[b_low_df["enlem"]==e_low].index
    bl_eh_ind = b_low_df[b_low_df["enlem"]==e_high].index
    bh_el_ind = b_high_df[b_high_df["enlem"]==e_low].index
    bh_eh_ind = b_high_df[b_high_df["enlem"]==e_high].index
    
  
    if len(bl_el_ind)!= 0 or len(bl_eh_ind)!= 0 or len(bh_el_ind)!= 0 or len(bh_eh_ind)!= 0:
        # Koordinatlara ait ss değeri
        bl_el_ss = float(df.iloc[bl_el_ind]["ss-10"])       # A noktası     0,      0
        bl_eh_ss = float(df.iloc[bl_eh_ind]["ss-10"])       # B noktası     0,      0.05
        bh_el_ss = float(df.iloc[bh_el_ind]["ss-10"])       # C noktası     0.05,   0
        bh_eh_ss = float(df.iloc[bh_eh_ind]["ss-10"])       # D noktası     0.05,   0.05
        
        a = [b_low, e_low, bl_el_ss] 
        b = [b_low, e_high, bl_eh_ss]
        c = [b_high, e_low, bh_el_ss]
        d = [b_high, e_high, bh_eh_ss]

        Ss = CalculatEz(boylam, enlem, a, b, c, d)

        Sds = CalculateSds(Ss, zemin)

        #ss_array = np.array([[bl_el_ss, bh_el_ss],
        #                     [bl_eh_ss, bh_eh_ss]])
        # b_low, b_high, e_low, e_high, a, b, c, d, Ss
        return round(Ss, 2), round(Sds, 2)

        
    else:
        return "Koordinatlar harita dışında"

def CalculatEz(boylam, enlem, A, B, C, D):
    E= [boylam, enlem]
    #A-B  Enlem
    AB_E = (abs(E[1]-B[1])*A[2]*10) + (abs(E[1]-A[1])*B[2]*10)
    #C-D Enlem
    CD_E = (abs(E[1]-D[1])*C[2]*10) + (abs(E[1]-C[1])*D[2]*10)
    #AB_E-CD_E boylam
    Ez = (abs(E[0]-C[0])*AB_E*10) + (abs(E[0]-A[0])*CD_E*10)
    
    return Ez

def CalculateSds(Ss, zemin):
    # https://github.com/gtuinsaat/TBDY2018_tepki_spektrumu
    Ss_range = [0.25 , 0.50 , 0.75, 1.00 , 1.25 , 1.50 ]
    FS_table = {"ZA": [0.8 , 0.8 , 0.8 , 0.8 , 0.8 , 0.8], 
                "ZB": [0.9 , 0.9 , 0.9 , 0.9 , 0.9 , 0.9], 
                "ZC": [1.3 , 1.3 , 1.2 , 1.2 , 1.2 , 1.2],
                "ZD": [1.6 , 1.4 , 1.2 , 1.1 , 1.0 , 1.0],
                "ZE": [2.4 , 1.7 , 1.3 , 1.1 , 0.9 , 0.8]}

    # Kısa periyod hesabı
    if Ss < Ss_range[0]:
        FS_satir = np.polyfit(Ss_range[0:2], list(FS_table[zemin])[0:2], 1)
        FS_katsayisi = np.poly1d( FS_satir )
        Fs = float( format(FS_katsayisi(Ss) , '.2f') )
        Sds = Ss * Fs
    elif Ss > Ss_range[-1]:
        FS_satir = np.polyfit(Ss_range[-3:-1], list(FS_table[zemin])[-3:-1], 1)
        FS_katsayisi = np.poly1d( FS_satir )
        Fs = float( format(FS_katsayisi(Ss) , '.2f') )
        Sds = Ss * Fs    
    else:
        FS_satir = interp1d(Ss_range, FS_table[zemin], kind='linear')
        FS_katsayisi = FS_satir(Ss)
        Fs = round( float(FS_katsayisi) , 2) 
        Sds = Ss * Fs

    return Sds
 


# input: enlem, boylam, zemin
#print(getAccCoeff(40.808495, 29.390368, "ZA"))
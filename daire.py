ARA_KAT=2
UST_KAT=1.6
ZEMIN_KAT=0.9
def daire_alan(en,boy):
    daire_a = en * boy
    return daire_a
def daire_fiyat(kat,en,boy):
    if kat == 0:
        katsayi = ARA_KAT
    elif kat == 1:
        katsayi = UST_KAT
    else:
        katsayi = ZEMIN_KAT
    fiyat = katsayi*daire_alan(en,boy)*5000
    return fiyat
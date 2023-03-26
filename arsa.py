import math

deniz_kenari = 1.6
kirsal = 0.8
sehir_merkezi = 1.2
bolge_katsayisi = [1.6,0.8,1.2]
def dikdortgen_cevre(en,boy):
    cevre_d = (2*en)+(2*boy)
    return cevre_d
def cember_cevre(r):
    cevre_daire = 2*math.pi*r
    return cevre_daire
def dikdörtgen_fiyat(i,en,boy):
    a_fiyat = bolge_katsayisi[i] * dikdortgen_cevre(en,boy)*1000
    return a_fiyat
def cember_fiyat(i,r):
    c_fiyat = bolge_katsayisi[i] * cember_cevre(r)*1000
    return c_fiyat





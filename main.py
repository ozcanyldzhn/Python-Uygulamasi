from arsa import dikdortgen_cevre,cember_cevre,dikdörtgen_fiyat,cember_fiyat
import daire
while True:
    secim=int(input("Arsa veya Daire için fiyat seçiniz(1-Arsa 2-Daire):"))
    if secim == 1:
        i = int(input("Arsa bölgesi nerede?(0-Deniz Kenarı,1-Kırsal,2-Şehir merkezi):"))
        cevre_secim =int(input("Arsa çevresi dikdörtgen mi? Çember mi? Seçiniz(1-Dikdörtgen,2-Çember):"))
        if cevre_secim == 1:
            en = float(input("Bir en değeri giriniz:"))
            boy = float(input("Bir boy degeri giriniz:"))
            cevre= dikdortgen_cevre(en,boy)
            print("Arsanın çevresi:",cevre)
            print("Arsa Fiyatı:",dikdörtgen_fiyat(i,en,boy))
        elif cevre_secim ==2:
            global r
            r=int(input("r gir:"))
            cevre = cember_cevre(r)
            print("Çember Çevresi",cevre)
            print("Arsanın Fiyatı:",cember_fiyat(i,r))
    elif secim==2:
        en = float(input("Bir En Değeri Giriniz:"))
        boy = float(input("Bir boy degeri giriniz:"))
        kat=int(input("Dairenin katı nedir(0-Ara Kat,1-Üst Kat,2-Zemin Kat):"))
        alan = daire.daire_alan(en,boy)
        daire_fiyat = daire.daire_fiyat(kat,en,boy)
        print("Dairenin alanı:",alan)
        print("Dairenin Fiyatı:",daire_fiyat)
    cevap=input("Devam etmeh istiyor musun? Evet(e)/Hayır(h):")
    if cevap.lower() == "e":
        continue
    elif cevap.lower() == "h":
        break

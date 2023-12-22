import time

worexmenu = []

def worexmenu_func():
    print("\033[91m===============================")
    print("|      WOREX industries       |")
    print("===============================\033[0m")
    time.sleep(2)

    while True:
        menu_goster()

def menu_goster():
    print("╔════════════════════════════╗")
    print("|     WOREX REHBER MENÜSÜ    |")
    print("|                            |")
    print("| 1- Kişi Ekle               |")
    print("| 2- Kişi Ara                |")
    print("| 3- Kişileri Görüntüle      |")
    print("| 4- Kişi Düzenle            |")
    print("| 5- Kişi Sil                |")
    print("| 6- Çıkış                   |")
    print("╚════════════════════════════╝")

    worex_secim = input("Lütfen bir işlem seçin (1-6): ")

    if worex_secim == "1":
        kisi_ekle()
    elif worex_secim == "2":
        kisi_ara()
    elif worex_secim == "3":
        kisileri_goruntule()
    elif worex_secim == "4":
        kisi_duzenle()
    elif worex_secim == "5":
        kisi_sil()
    elif worex_secim == "6":
        print("Telefon Rehberi Uygulaması kapatılıyor. İyi günler!")
        log_kaydet("Uygulama kapatıldı.")
        time.sleep(2)
        exit()
    else:
        print("Geçersiz seçim. Lütfen 1 ile 6 arasında bir sayı girin.")

def kisileri_goruntule():
    print("\nKişiler:")
    if not worexmenu:
        print("Hiç kişi bulunamadı.")
    else:
        for kisi in worexmenu:
            print("\n--------\nAd: {}\nSoyad: {}\nNumara: {}".format(*kisi.values()))
    print()
    log_kaydet(f"-------------------------\n{tarih_saat()}\nKişiler görüntülendi.\n")

def kisi_ara():
    worex_isim_ara = input("Aranacak kişinin adını girin: ")
    bulunan_kisiler = [kisi for kisi in worexmenu if worex_isim_ara.lower() in kisi['Ad'].lower()]
    if not bulunan_kisiler:
        print(f"'{worex_isim_ara}' adında hiç kişi bulunamadı.")
    else:
        print("\nBulunan Kişiler:")
        for kisi in bulunan_kisiler:
            print("\n--------\nAd: {}\nSoyad: {}\nNumara: {}".format(*kisi.values()))
        print()
    log_kaydet(f"-------------------------\n{tarih_saat()}\n'{worex_isim_ara}' adında kişi arandı.\n")

def kisi_ekle():
    ad = input("Adı girin: ")
    soyad = input("Soyadı girin: ")
    numara = input("Numarayı girin: ")
    yeni_kisi = {"Ad": ad, "Soyad": soyad, "Numara": numara}
    worexmenu.append(yeni_kisi)
    print(f"{ad} kişisi başarıyla eklendi.")
    log_kaydet(f"-------------------------\n{tarih_saat()}\nKişi Eklendi:\nAd: {ad}\nSoyad: {soyad}\nNumara: {numara}\n")

def kisi_duzenle():
    worex_isim_duzenle = input("Düzenlenecek kişinin adını girin: ")
    worex_kisi_duzenleler = [kisi for kisi in worexmenu if worex_isim_duzenle.lower() in kisi['Ad'].lower()]
    if not worex_kisi_duzenleler:
        print(f"'{worex_isim_duzenle}' adında hiç kişi bulunamadı.")
    else:
        print("\nDüzenlenecek Kişiler:")
        for i, kisi in enumerate(worex_kisi_duzenleler, 1):
            print("\n--------\nAd: {}\nSoyad: {}\nNumara: {}".format(*kisi.values()))
        secim = input("Lütfen düzenlenecek kişiyi seçin (1-{}): ".format(len(worex_kisi_duzenleler)))
        try:
            secim = int(secim)
            if 1 <= secim <= len(worex_kisi_duzenleler):
                secilen_kisi = worex_kisi_duzenleler[secim - 1]
                yeni_ad = input("Yeni adı girin (eski ad: {}): ".format(secilen_kisi['Ad']))
                yeni_soyad = input("Yeni soyadı girin (eski soyad: {}): ".format(secilen_kisi['Soyad']))
                yeni_numara = input("Yeni numarayı girin (eski numara: {}): ".format(secilen_kisi['Numara']))
                secilen_kisi['Ad'] = yeni_ad
                secilen_kisi['Soyad'] = yeni_soyad
                secilen_kisi['Numara'] = yeni_numara
                print(f"{secilen_kisi['Ad']} kişisi başarıyla güncellendi.")
                log_kaydet(f"-------------------------\n{tarih_saat()}\nKişi Güncellendi:\nEski Ad: {secilen_kisi['Ad']}\nEski Soyad: {secilen_kisi['Soyad']}\nEski Numara: {secilen_kisi['Numara']}\nYeni Ad: {yeni_ad}\nYeni Soyad: {yeni_soyad}\nYeni Numara: {yeni_numara}\n")
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Geçersiz giriş. Bir sayı girin.")

def kisi_sil():
    worex_isim_sil = input("Silinecek kişinin adını girin: ")
    worex_kisi_sil = [kisi for kisi in worexmenu if worex_isim_sil.lower() in kisi['Ad'].lower()]
    if not worex_kisi_sil:
        print(f"'{worex_isim_sil}' adında hiç kişi bulunamadı.")
    else:
        print("\nSilinecek Kişiler:")
        for i, kisi in enumerate(worex_kisi_sil, 1):
            print("\n--------\nAd: {}\nSoyad: {}\nNumara: {}".format(*kisi.values()))
        secim = input("Lütfen silinecek kişiyi seçin (1-{}): ".format(len(worex_kisi_sil)))
        try:
            secim = int(secim)
            if 1 <= secim <= len(worex_kisi_sil):
                silinecek_kisi = worex_kisi_sil[secim - 1]
                worexmenu.remove(silinecek_kisi)
                print(f"{silinecek_kisi['Ad']} kişisi başarıyla silindi.")
                log_kaydet(f"-------------------------\n{tarih_saat()}\nKişi Silindi:\nAd: {silinecek_kisi['Ad']}\nSoyad: {silinecek_kisi['Soyad']}\nNumara: {silinecek_kisi['Numara']}\n")
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Geçersiz giriş. Bir sayı girin.")

def log_kaydet(log_mesaji):
    with open("worex_logg.txt", "a") as worex_logg:
        worex_logg.write(log_mesaji)

def tarih_saat():
    return time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    worexmenu_func()

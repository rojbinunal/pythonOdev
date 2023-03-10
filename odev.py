# 1-  Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazın

# String Veri Tipi : Metinsel veri tipleri için kullanılır ve " " içinde yazılır. (örneğin ad = "Rojbin")

# Integer (int) Veri Tipi : Tam sayı değerleri için kullanılır. (örneğin kisiSayisi = 21)

# Float Veri Tipi : Ondalıklı sayı değerleri için kullanılır. (örneğin kgDegeri = 10.8)

# Boolean Veri Tipi : Mantıksal bir veri tipidir. True ve False değerlerini alır. (örneğin a = 5 , if (a%2==0), False )


# 2- Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# String Veri Tipine Örnekler : Kursun ismi, eğitmenin bilgileri, kurs tanıtımı 
# Integer Veri Tipine Örnekler : Yorum sayısı, kursun tamamlanma oranı 
# Boolean Veri Tipine Örnekler : Kurstaki bir kısmın tamamlanıp tamamlanmadığı 



# 3- Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.



kullaniciMail = "aaaa@gmail.com"
kullaniciSifre = "1234"

mail = input("Mail adresinizi giriniz")
sifre = input("Şifrenizi giriniz")


if kullaniciMail == mail and kullaniciSifre !=sifre:
    print("Şifre Hatalı")

if kullaniciMail != mail and kullaniciSifre ==sifre:
    print("Mail adresi hatalı")

elif kullaniciMail == mail and kullaniciSifre == sifre:
    print("Başarıyla giriş yapıldı")

else:
    print("Sistemde böyle bir kayıt bulunamadı")

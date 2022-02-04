# Fonksiyonlar, yalnızca çağrıldığında çalışan bir kod bloklarıdır. 
# Parametre olarak bilinen verileri bir fonksiyonda kullanabilirsiniz.

#Fonksiyon Kullanımı
def fonksiyon():
  print("Merhaba, ben fonksiyonum.")
  
#Fonksiyon Çağırma
def fonksiyon():
  print("Merhaba, ben fonksiyonum.")
  
fonksiyon()

#Fonksiyonlara Parametre Ekleme
def fonksiyon(selamlama):
    print(selamlama + " ben fonksiyonum.")
    
fonksiyon("Merhaba")

#Örnek-2
def fonksiyon(carName):
    print("Marka: " + carName)
    
fonksiyon("BMW")

#Fonksiyonlara birden fazla parametre ekleme
def fonksiyon(carName, yılı):
    print("Arabanin markasi " + carName + " olup " + str(yılı) + " modeldir.")

fonksiyon("BMW", 2018)

#Örnek-3
def fonksiyon(bilgisayarMarka, bRenk, bEkranKarti):
    print("Bilgisayarin markasi "+bilgisayarMarka+ " olup rengi "+bRenk+" ve icerisinde "+bEkranKarti+" mevcuttur.")
    
fonksiyon("MSI", "Siyah", "GTX 1050")

#Fonksiyonunuza kaç adet parametre ekleyeceğinizi bilmiyorsanız, parametre sayısının sınırını belirtmek için * kullanabilirsiniz.
def fonksiyonum(*cocuklar):
      print("En genc cocuk " + cocuklar[1])

fonksiyonum("Emre", "Yagiz", "Efe")

#Anahtar kelime parametrelerinin sayısı bilinmiyorsa, parametre adından önce bir çift ** ekleyin
def fonksiyonum(**cocuk):
      print("Onun soyadi " + cocuk["soyAdi"])

fonksiyonum(adi = "Yunus Emre", soyAdi = "Yakisan")

#Fonksiyonu argümansız (parametresiz) çağırırsak, varsayılan değeri kullanır.
def fonksiyon1(takimAdi = "GS"):
    print("Muslera " + takimAdi + " takimimdeki bir futbolcu.")

fonksiyon1()



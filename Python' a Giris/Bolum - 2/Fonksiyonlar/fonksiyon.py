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

#Bir fonksiyonun bir değer döndürmesine izin vermek için return ifadesini kullanırız.
def fonksiyon2(x):
   return 5 * x
    
print(fonksiyon2(5))
print(fonksiyon2(2))

#Özyineleme, ortak bir matematik ve programlama kavramıdır. Bu, bir işlevin kendisini çağırdığı anlamına gelir.
#Bu, bir sonuca ulaşmak için veriler arasında dolaşabileceğiniz anlamına gelir.
'''Yeni bir geliştirici için bunun tam olarak nasıl çalıştığını anlaması biraz zaman alabilir, öğrenmenin en iyi yolu onu test etmek ve değiştirmektir.'''

def yineleme(k):
  if(k > 0):
    sonuc = k + yineleme(k - 1)
    print(sonuc)
  else:
    sonuc = 0
  return sonuc
yineleme(6) #Kaça kadar devam edeceğini söyler.


'''Anlaman için buraya yorum satırı olarak yazıyorum.'''

# ilk olarak k yerine 1 verdim.
#def yineleme(1):
#   if(1> 0):
#     sonuc = 1 + yineleme(1 - 1) [yineleme sıfır oldu burda sonra başa aldım şimdi 0 üzerinden bakıyorum.] yineleme(0) a bakıyorum.
#     print(sonuc)
#   else:
#     sonuc = 0
#   return sonuc
# yineleme(6)

# Şimdi k yerine 2 veriyorum.
# 2 verdim sonuc = 2 + yineleme(2-1)
# sonuc = 2 + yineleme(1) oldu
# şimdi yineleme(1) başa yazıp fonksiyonu döndüreceğim.
# döndürdükten sonra 1+0 = 1 oluyor. k yerine 2 yazdığımdan 2 geldi.
# 2+1 = 3 oluyor.

# devam ediyorum. 3 veriyorum.
# sonuc = 3 + yineleme(2)
# yineleme(2) yukarıda buldum 3 çıkmıştı.
# sonuc = 3 + 3 = 6
'''k yerine 6 verene kadar devam ediyorum.'''

#Bir lambda fonksiyonu, küçük bir anonim fonksiyondur. Bir lambda fonksiyonu herhangi bir sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir.

#Lambda kullanımı
x = lambda a : a + 10 #a değişkenine 10 eklenip döndürülür.
print(x(5))

#Lambda işlevleri herhangi bir sayıda parametre alabilir.
x = lambda a, b : a * b
print(x(5, 6))
#Kalıtım, tüm yöntemleri ve özellikleri başka bir sınıftan miras alan bir sınıf tanımlamamızı sağlar. 
#Üst sınıf, temel sınıf olarak da adlandırılan, miras alınan sınıftır.
#Alt sınıf, türetilmiş sınıf olarak da adlandırılan başka bir sınıftan miras alan sınıftır.

#Miras Kullanımı
class Insan:
      def __init__(self, adi, soyAdi):
        self.adi = adi
        self.soyadi = soyAdi

      def adYazdır(self):
        print(self.adi, self.soyadi)

#Bir nesne oluşturmak için Insan sınıfını kullanın ve ardından adYazdir() yöntemini çalıştırın:
x = Insan("Yunus Emre", "Yakisan")
x.adYazdır()

#Çocuk Sınıf Oluşturma 
class Ogrenci(Insan):
      pass

'''NOT : Sınıfa başka özellikler veya yöntemler eklemek istemiyorsanız pass anahtar sözcüğünü kullanın.'''

#Alt sınıfa (pass anahtar sözcüğü yerine) __init__() işlevini eklemek istiyoruz.
class Ogrenci(Insan):
    def __init__(self, adi, soyAdi, no):
        Insan.__init__(self, adi, soyAdi)
        self.no = no       
#__init__() işlevi, sınıf yeni bir nesne oluşturmak için her kullanıldığında otomatik olarak çağrılır.







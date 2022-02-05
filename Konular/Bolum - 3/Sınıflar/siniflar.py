# Python, nesne yönelimli bir programlama dilidir. 
# Python'daki hemen hemen her şey, özellikleri ve yöntemleri ile bir nesnedir.

#Sınıf oluşturma 
class Sinifim:
  x = 5
  
#Nesne oluşturma 
p1 = Sinifim()
print(p1.x)

#Kişi adında bir sınıf oluşturun, ad ve yaş için değerler atamak için __init__() işlevini kullanın
class Insan:
      def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

p1 = Insan("Yunus Emre", 21)

print(p1.ad)
print(p1.yas)

#Nesne Metodları
class Insan:
    def __init__(self, ad, yas): 
        self.ad = ad
        self.yas = yas

    def fonksiyon(self): #self ile özellikleri ve yöntemleri çağırabiliriz.
        print("Merhaba, benim adim " + self.ad) #self.ad ile değişkenleri kullanabilirsiniz.
 
p1 = Insan("Yunus Emre", "21")
p1.fonksiyon()

'''NOT: self parametresi, sınıfın mevcut örneğine bir referanstır. 
Sınıfa ait değişkenlere erişmek için kullanılır.
Self olarak adlandırılması gerekmez, istediğiniz gibi adlandırabilirsiniz, ancak sınıftaki herhangi bir işlevin ilk parametresi olmalıdır.'''

#Örnek-1
class Insan:
    def __init__(ref, ad, yas): 
        ref.ad = ad
        ref.yas = yas

    def fonksiyon(ref): #ref ile özellikleri ve yöntemleri çağırabiliriz.
        print("Merhaba, benim yasim " + ref.yas) #ref.yas ile değişkenleri kullanabilirsiniz.
 
p1 = Insan("Yunus Emre", "21")
p2 = Insan("Yagiz Erhan", "2")
p1.fonksiyon()

#Aşağıdaki gibi nesnelerdeki özellikleri de değiştirebilirsiniz.
p1.yas = "40"
print(p1.yas)

#Del anahtar sözcüğünü kullanarak nesnelerdeki özellikleri silebilirsiniz
del p1.yas
print(p1.yas) #Özellik silindiği için hata verecektir. 
'''AttributeError: 'Insan' object has no attribute 'yas''' #Hata mesajı

#Del anahtar sözcüğünü kullanarak nesneleri silebilirsiniz.
del p1
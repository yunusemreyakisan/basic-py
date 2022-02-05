# Yerel Kapsam, bir fonksiyon içinde yaratılan bir değişken, o fonksiyonun yerel kapsamına aittir ve sadece o fonksiyonun içinde kullanılabilir.

def fonksiyon():
      x = 300
      print(x)
fonksiyon()

#Fonksiyon içinde fonksiyon kullanımı
def fonksiyonum():
   x = 150 #Fonksiyon içinde x değişkeni tanımlanır.
   def icfonksiyon():
     print(x)
     icfonksiyon()
     print(fonksiyonum())


# Küresel Kapsam, Python kodunun ana gövdesinde oluşturulan bir değişken global bir değişkendir ve global kapsama aittir. 
# Global değişkenler, global ve yerel herhangi bir kapsamda kullanılabilir.
x = 200 # Global
def myfunc():
  print(x)
myfunc()
print(x)

def myfunc1():
    global x #Burada global kapsamına girmek istiyoruz.
    x = 300
myfunc1()
print(x)
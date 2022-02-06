#Tuple, veri koleksiyonlarını depolamak için kullanılan Python'da yerleşik 4 veri türünden biridir, diğer 3'ü List, Set ve Dictionary'dir ve tümü farklı niteliklere ve kullanıma sahiptir.
# Not : Tuple yuvarlak parantez ile yazılır.

#Tuple oluşturma
mytuple = ("Elma", "Muz", "Çilek")

#Tuple uzunluğunu öğrenme 
mytuple = ("Elma", "Muz", "Çilek")
print(len(mytuple))

#Tuple, string, tamsayılar ve boole değerleri içeren bir örnek:
tuple1 = ("abc", 34, True, 40, "male") 

#Tuple içerisindeki elemanların tipini öğrenme
mytuple = ("Elma", "Muz", "Çilek")
print(type(mytuple[2]))

#Tuple içerisindeki değerleri değiştirme 
mytuple = ("Elma", "Muz", "Çilek")
x = list(mytuple) #Tuple içerisindeki değerleri değiştirmek için listeye çeviriyoruz.
x[1] = "Kavun"
x = tuple(x)
print(x)

#Tuple içerisine veri ekleme
mytuple = ("Elma", "Muz", "Çilek")
y = list(mytuple) #Veri eklemek için listeye çeviriyoruz.
y.append("Kavun")
mytuple= tuple(y)
print(mytuple)

#Tuple içerisinden veri silme
mytuple = ("Elma", "Muz", "Çilek")
a = list(mytuple)
a.remove("Elma")
mytuple= tuple(a)
print(mytuple)

#Birden fazla Tuple dizisini birleştirme
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Tuple Metodları    
# count() : Bir tanımlama grubunda belirtilen bir değerin kaç kez oluştuğunu döndürür.
# index() : Tuple'ı belirtilen bir değer için arar ve bulunduğu yerin konumunu döndürür.
#String Karakter Tanımlama
name = "Yunus Emre"
surname="Yakisan"
greeting = "My name is "+ name + " "+surname
#print(greeting)
print(greeting[0]) #0.indeksteki elemanı yazdırır.
print(greeting[-2]) #Sondan 2. elemanı yazdırır.
print(greeting[3:5]) #3.indeksten 5.indekse kadar yazdırır.
print(greeting[4:]) #4.indeksten başlar, sona kadar yazdırır.
print(greeting[2:40:2]) #2.indeksten 40. indekse kadar git ama 2 karakterde bir alıp yazdırır.


#String Formatlama
name = "Emre"
surname= "Yakışan"
print("My name is {} {}".format(name, surname)) #format metodu ile ekrana yazdırılır.
print("My name is {1} {0}".format(name, surname)) #surname ilk yazılır, sonrası name yazdırılır.
print("My name is {s} {n}".format(n = name, s = surname)) #surname ilk yazdırılır, sonra name yazdırılır.

result = 200/700
print("Sonuç {r:1.2}".format(r = result)) #Sonucun başında ne kadar boşluk olacağını ve sonrasında kaç basamak yazdırılacağını belirtir.

#Uygulama

#Soru-1 : 'course' içerisinden ilk 15 ve son 15 karakteri alın.
kelime = 'course'
print(kelime[:5]) #5.indeksten geriye doğru yazdırır.
print(kelime[3:]) #3.indeksten sonra yazdırır.

#Soru-2 : Aşağıda verilen değişkenler ile ekrana şu ifadeyi yazdırın.
#Yazdırılacak ifade : Benim adım Yunus Emre Yakışan, yaşım 21 ve mesleğim Mühendis.
name1, surname1, age1, job1 = 'Yunus Emre', 'Yakışan', 21, 'Mühendis'
print('Benim adım {} {}, yaşım {} ve mesleğim {}'.format(name1, surname1, age1, job1))
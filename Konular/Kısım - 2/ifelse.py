# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# if else yazımı
a = 33
b = 200
if b > a:
  print("B sayisi A sayisindan daha buyuktur.")
  
# if-else yapısında ekrana yazdırmak için bir boşluk bırakınız.
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # hata alırız.

# elif, Python'un "önceki koşullar doğru değilse bu koşulu dene" demenin yoludur.
a = 33
b = 33
if b > a:
  print("B sayisi A sayisindan daha buyuktur.")
elif a == b:
  print("A sayisi ile B sayisi esittir.") #yazdırma işlemi bir adım ileride unutma.
  
  
#else yazımı
a = 33
b = 32
if b > a:
  print("B sayisi A sayisindan daha buyuktur.")
elif a == b:
  print("A sayisi ile B sayisi esittir.")
else: 
    print("A sayisi ile B sayisi esit degildir.")
    
#Kısa şekilde if-else yapısını yazdırma
if a > b: print("A sayisi B sayisindan daha buyuktur.")

a = 2
b = 330
print("A") if a > b else print("B")  

'''OPERATÖRLER'''

#AND operatörünü kullanma   
a = 200
b = 33
c = 500
if a > b and c > a: #Buradaki değerlerin ikisi de sağlamalıdır. Sağlanmazsa else yapısına atılır.
  print("Her iki koşuldan da saglanir.")
  

#OR operatörünü kullanma
a = 200
b = 33
c = 500
if a > b or a > c: #Koşullardan herhangi birisinin doğru olması yeterlidir.
  print("Koşullardan birisi doğru.") 
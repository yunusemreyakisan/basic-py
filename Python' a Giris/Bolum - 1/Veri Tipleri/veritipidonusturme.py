#Veri Tipi Dönüştürme

k = 5               #int
s = 6.3             #float
kisi = 'Emre'       #String

print(type(k))
print(type(s))
print(type(kisi))

k= float(k)
print(k)
print(type(k))

#Uygulama
pi= 3.14
yariCap= float(input("Bir yaricap giriniz: "))
alan = (pi*yariCap*yariCap)
cevre= (2*pi*yariCap)

alan = int(alan)
cevre= int(cevre)
print("Alan: ", alan, "Cevresi: ", cevre)
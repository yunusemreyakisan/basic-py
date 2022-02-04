#Bir for döngüsü (bir liste, bir tuple, bir sözlük, bir küme veya bir dize) üzerinde yineleme yapmak için kullanılır.

#for döngüsü kullanımı
fruits = ["Elma", "Muz", "Çilek"]
for x in fruits: #fruits listesindeki her bir elemanı x değişkenine atar.
  print(x)

#Dizi içerisindeki elemanı aramak
for x in "Muz": #Muz kelimesi içeren bir dizi içerisinde arama yapar.
  print(x)

#Break ifadesi ile, tüm öğeler arasında döngü oluşturmadan önce döngüyü durdurabilirsin.
fruits = ["Elma", "Muz", "Çilek"]
for x in fruits:
  print(x)
  if x == "Muz": 
    break 

#continue kullanımı
fruits = ["Elma", "Muz", "Çilek"]
for x in fruits:
  if x == "Elma":
    continue 
  print(x)

#Kaça kadar döngü yapacağınızı belirtmek için range() fonksiyonunu kullanabilirsiniz.
for x in range(6):
    print(x)
      
'''Not: range(6)'nın 0 ila 6 arasındaki değerler değil, 0 ila 5 arasındaki değerler olduğuna dikkat edin.'''

#range(2, 6), bu da 2 ile 6 arasındaki değerler anlamına gelir.(ancak 6 dahil değildir.)
for x in range(2, 6):
    print(x)

#Döngü bittiğinde else bloğu çalışır.
for x in range(6):
      if x == 3: break
      print(x) 
else:
  print("Sonunda bitti!")

#İç içe for döngüsü kullanımı 
sifat = ["Kırmızı", "Büyük", "Tatlı"]
fruits = ["Elma", "Muz", "Çilek"]

for x in sifat:
  for y in fruits:
    print(x, y)
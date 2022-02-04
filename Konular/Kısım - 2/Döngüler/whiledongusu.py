#while döngüsü ile bir koşul doğru olduğu sürece bir dizi ifadeyi çalıştırabilirsiniz.

#while kullanımı
i = 1
while i < 6: #i değeri 6'e eşit olana kadar devam eder.
  print(i)
  i += 1 #i değerini 1 arttırır.

#break durumu kullanımı
i = 1
while i < 6: #i değeri 6'e eşit olana kadar devam eder.
  print(i)
  if i == 3: #i değeri 3'e eşitse
    break #döngüden çıkılır.
  i += 1 
  
#continue durumu kullanımı
i = 0
while i < 6: #i değeri 6'e eşit olana kadar devam eder.
  i += 1
  if i == 3: 
    continue #i değeri 3'e eşitse devam eder.
  print(i)

#else durumu kullanımı
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i artik 6 sayisindan büyük.") #i değeri 6 dan büyük olduğu için direkt çıkar.
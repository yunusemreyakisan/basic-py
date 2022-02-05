'''JSON, verileri depolamak ve değiştirmek için bir sözdizimidir.'''

#JSON modülünü eklemek
import json

#JSON'dan Python'a dönüştürme.
import json
# JSON:
x =  '{ "isim":"Yunus Emre", "yas":21, "sehir":"Bursa"}'
# JSON ayrıştırma:
y = json.loads(x)
# JSON'u Python'a dönüştürme:
print(y["age"])

#Python'dan JSON'a Dönüştürme
import json
# Python'dan JSON'a dönüştürme:
x = {
  "isim": "Yunus Emre",
  "yas": 21,
  "sehir": "Bursa"
}
# json'a dönüştürme:
y = json.dumps(x)
# JSON'u yazdırma:
print(y)

# Python nesnelerini JSON dizelerine dönüştürün ve değerleri yazdırın.
import json

print(json.dumps({"isim": "Yunus Emre", "age": 21})) #Python nesnelerini JSON dizelerine dönüştürün ve değerleri yazdırın.
print(json.dumps(["Elma", "Muz"])) # Listeler
print(json.dumps(("Elma", "Muz"))) #Tuple
print(json.dumps("hello")) #String
print(json.dumps(42)) #Sayı
print(json.dumps(31.76)) #Sayı
print(json.dumps(True)) #Boolean
print(json.dumps(False)) #Boolean
print(json.dumps(None)) #None

# Örnek-3: Tüm yasal veri türlerini içeren bir Python nesnesini dönüştürün.
import json

x = {
  "isim": "Yunus Emre",
  "yas": 21,
  "medenihal": False,
  "evcilhayvan": None,
  "araba": [
    {"model": "BMW 230", "km": 27.5},
    {"model": "Ford Edge", "km": 24.1}
  ]
}

print(json.dumps(x))

'''Python Kullanıcı Girişi''' #Python 3.6
kullaniciadi = input("Kuulanici adinizi giriniz:")
print("Kullanici adiniz: " + kullaniciadi)



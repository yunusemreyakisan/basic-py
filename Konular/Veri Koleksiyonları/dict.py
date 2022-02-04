# Dict, veri koleksiyonlarını depolamak için kullanılan Python'da yerleşik 4 veri türünden biridir, diğer 3'ü Tuple, List ve Set'dir ve tümü farklı niteliklere ve kullanıma sahiptir.
# Python 3.7 sürümünden itibaren sözlükler sıralanmıştır. Python 3.6 ve önceki sürümlerde sözlükler sırasızdır.
# Sözlükler, veri değerlerini anahtar:değer çiftlerinde depolamak için kullanılır. Sözlük, sıralı*, değiştirilebilir ve kopyalara izin vermeyen bir koleksiyondur.

#Dict oluşturma
thisdict = {
  "marka": "Ford",
  "model": "Mustang",
  "yılı": 1964
}

#Dict içerisinden veriyi yazdırma 
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}
print(thisdict["marka"])

#Dict, tekrarlanan elemanlar için en son yazılanı kabul eder.
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016,
  "yılı": 2022,
}
print(thisdict)

#Dict dizisi boyutunu öğrenme  
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}
print(len(thisdict))

#Veri Tipleri
thisdict = {
  "marka": "Ford", #String
  "dizel mi": False,#boolean
  "yılı": 1964, #Integer
  "renk": ["Kırmızı", "Beyaz", "Mavi"] #List
}

#Dict veri tipini yazdırma 
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}
print(type(thisdict)) #dict

#Dict üzerindeki verilere ulaşma ve veriyi çekme
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}
x = thisdict["marka"]
print(x)

a = thisdict.get("yılı")
print(a)

key = thisdict.keys() #Anahtar kelimeleri alır.
print(key)

thisdict["year"] = 2018 #Dict içerisindeki elemanı değiştirme
print(thisdict.get("year"))

#Dict içerisine veri ekleme 
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}

thisdict["renk"] = "Kırmızı" #Veri ekleme
print(thisdict)

thisdict.update({"renk": "Siyah"}) #Rengi güncelleme

#Döngü ile dizi elemanlarını dolaşma
thisdict = {
  "marka": "Volvo",
  "model": "S90",
  "yılı": 2016
}

for x in thisdict:
      print(thisdict[x])

#İç içe diziler
myfamily = {
  "cocuk1" : {
    "isim" : "Emre",
    "yılı" : 2000
  },
  "cocuk2" : {
    "isim" : "Efe",
    "yılı" : 2005
  },
  "child3" : {
    "isim" : "Yağız",
    "yılı" : 2020
  }
}
print(myfamily) #Dict içerisindeki iç içe dizileri gösterir.

#Kodları yazdığım sırada Github Copilot teknik izlenimine kabul aldım.
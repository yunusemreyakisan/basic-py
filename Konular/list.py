# # Listeler, veri koleksiyonlarını depolamak için kullanılan Python'da yerleşik 4 veri türünden biridir, diğer 3'ü Tuple, Set ve Dictionary'dir ve tümü farklı niteliklere ve kullanıma sahiptir.

# #Liste Oluşturma
# list = ["Elma", "Muz", "Çilek"]
# print(list)

# # Liste öğeleri indekslenir.
# # İlk öğenin indeksi [0], ikinci öğenin indeksi [1] vb. devam eder.

# #Bir listenin boyutunu öğrenmek için len() fonksiyonunu kullanırız.
# list = ["Elma", "Muz", "Çilek"]
# print(len(list)) #3

# #Listenin tipini öğrenmek için type() sorgusu kullanırız.
# list = ["Elma", "Muz", "Çilek"]
# print(type(list)) #list

# #Liste Elemanlarına Erişme
# list = ["Elma", "Muz", "Çilek"]
# print(list[2]) #Çilek

# #Liste Elemanlarını Kontrol Etme
# list = ["Elma", "Muz", "Çilek"]
# if "Çilek" in list:
#     print("Evet, listede çilek maddesi var.")
    
# #Liste Elemanlarını Değiştirme
# list = ["Elma", "Muz", "Çilek"]
# list[2] = "Portakal"
# print(list)

#Liste elemanlarına sınır belirterek eleman ekleyebiliriz.
# list = ["Elma", "Muz", "Çilek"]
# list[0:1]= "Armut", "Vişne", "Kavun"
# print(list)

#Liste elemanlarını sınır belirterek değiştirebiliriz.
# list = ["Elma","Muz","Çilek"]
# list[0:3]= ["Armut", "Vişne", "Kavun"]
# print(list)

#Bir listede elemanları döngü kullanarak yazdırabiliriz.
# list = ["Elma","Muz","Çilek"]
# for x in list:
#  print(x)


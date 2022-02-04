# Set, veri koleksiyonlarını depolamak için kullanılan Python'da yerleşik 4 veri türünden biridir, diğer 3'ü Tuple, List ve Dictionary'dir ve tümü farklı niteliklere ve kullanıma sahiptir.

#Set oluşturma
myset = {"Elma", "Muz", "Çilek"}

#Not: Set öğeleri değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.
#Küme, sıralanmamış, değiştirilemez* ve indekslenmemiş bir koleksiyondur.

#Set ekrana yazdırma 
myset = {"Elma", "Muz", "Çilek"}
print(myset)

#Set boyutunu öğrenme 
myset = {"Elma", "Muz", "Çilek"}
print(len(myset))

#Set dizisine erişme 
myset = {"Elma", "Muz", "Çilek"}
for x in myset:
    print(x)
    
#Set dizisine eleman ekleme 
myset = {"Elma", "Muz", "Çilek"}
myset.add("Kavun")
print(myset)

#Set dizilerini birleştirme
myset = {"Elma", "Muz", "Çilek"}
set1 = {"Kırmızı", "Mavi", "Sarı"}

myset.update(set1)
print(myset)

#Set dizisinden herhangi bir elemanı silme
myset = {"Elma", "Muz", "Çilek"}
myset.remove("Elma")
print(myset)

#Set dizisinden son elemanı kaldırma 
myset = {"Elma", "Muz", "Çilek"}
myset.pop()
print(myset)
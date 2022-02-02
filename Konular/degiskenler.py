#Bir değişkenin kısa bir adı (x ve y gibi) veya daha açıklayıcı bir adı (yaş, carname, toplam_hacim) olabilir. 
#Python değişkenleri için kurallar:
# 1- Değişken adı bir harf veya alt çizgi karakteri ile başlamalıdır. 
# 2- Değişken adı bir sayı ile başlayamaz.
# 3- Değişken adı yalnızca alfasayısal karakterler ve alt çizgiler içerebilir. (A-z, 0-9 ve _ )
# 4- Değişken adları büyük/küçük harfe duyarlıdır. (yaş, Yaş ve YAŞ üç farklı değişkendir.)

# Ekrana herhangi bir şey yazdırma
print("Hello World")

#Değişkenleri sırasıyla atama ve yazdırma
a, c, name, isStudent = (1, 2, 'Emre', True )
print(a, c, name, isStudent)

#Değişken isimleri büyük/küçük harf duyarlıdır.
a = 4
A = "Yunus Emre" #A, a'nın üzerine yazılmaz. İkisi ayrı değişkenlerdir.

#Bazı doğru olan değişken ismi tanımlamaları:
# #myvar = "Emre"
# my_var = "Emre"
# _my_var = "Emre"
# myVar = "Emre"
# MYVAR = "Emre"
# myvar2 = "Emre"

#Doğru yazılmayan değişken adları:
#2myvar = "Emre"
#my-var = "Emre"
#my var = "Emre"

#Çoklu Kelime Değişken İsimleri
# Camel Case = myVariableName = "Emre"  | #İlk kelime hariç her kelime büyük harfle başlar.
# Pascal Case = MyVariableName = "Yunus" | #Her kelime büyük harfle başlar.
# Snake Case = my_variable_name = "Yakışan" | #Her kelime bir alt çizgi karakteri ile ayrılır.

#Uygulama
musAd = 'Yunus Emre '
musSoyad= "Yakisan"
musAdSoyad = musAd + musSoyad
musCins = 'Erkek'
musTC = 37646365487
musDogyil = 2000
musAdres = 'Arapzade Mah. Dr. Cemil Mandi Cad. No:19'
musYas = 21
print(musAdSoyad, musCins, musTC, musDogyil, musAdres, musYas)

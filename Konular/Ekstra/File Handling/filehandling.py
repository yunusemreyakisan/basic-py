# Dosya işleme, herhangi bir web uygulamasının önemli bir parçasıdır. Python'un dosya oluşturmak, okumak, güncellemek ve silmek için çeşitli işlevleri vardır.
'''Python'da dosyalarla çalışmanın temel işlevi open() işlevidir. open() işlevi iki parametre alır; dosya adı ve mod. Bir dosyayı açmak için dört farklı yöntem (mod) vardır.'''

# "r" - Okuma - Varsayılan değer. Okumak için bir dosya açar, dosya yoksa hata verir.
# "a" - Ekle - Eklemek üzere bir dosya açar, mevcut değilse dosyayı oluşturur.
# "w" - Yaz - Yazmak için bir dosya açar, yoksa dosyayı oluşturur. 
# "x" - Oluştur - Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür.

'''Ek olarak, dosyanın ikili veya metin modu olarak mı ele alınması gerektiğini belirleyebilirsiniz.'''
# "t" - Metin - Varsayılan değer. Metin modu 
# "b" - İkili - İkili mod (ör. resimler)

'''SYNTAX'''
f = open("demofile.txt")
#Not: Dosyanın var olduğundan emin olun, aksi takdirde bir hata alırsınız.

'''Sunucuda bir dosya açma'''
f = open("demofile.txt", "r") #Dosyayı açmak için yerleşik open() işlevini kullanın. 
print(f.read()) #Dosyayı okumak için read() işlevini kullanın.

#Dosya farklı bir konumda bulunuyorsa, dosya yolunu şu şekilde belirtmeniz gerekir:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#Satır Okuma
f = open("demofile.txt", "r")
print(f.readline()) #Dosyayı satır satır okumak için readline() işlevini kullanın.

#Örnek-1: Dosyayı satır satır dolaşın. 
f = open("demofile.txt", "r")
for x in f:
  print(x)

#Bitirdiğinizde dosyayı kapatın.
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Mevcut bir dosyaya yazdırıp okuma     
f = open("demofile2.txt", "a")
f.write("İçerik ekledim!") #Dosyayı yazmak için write() işlevini kullanın.
f.close()

f = open("demofile2.txt", "r") #Dosyayı tekrar açın.
print(f.read()) #Dosyayı okumak için read() işlevini kullanın.

#Dosya Silme 
import os
os.remove("demofile.txt") #Dosyayı silmek için os.remove() işlevini kullanın.

#Dosyanın var olup olmadığını kontrol edin, ardından silin.
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("Dosya yok!")

#Klasör Silme 
import os
os.rmdir("klasorum") 

'''Not: Yalnızca boş klasörleri kaldırabilirsiniz.'''
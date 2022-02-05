'''Python'da bir tarih, kendi başına bir veri türü değildir, ancak tarih nesneleri olarak tarihlerle çalışmak için datetime adlı bir modülü içe aktarabiliriz.'''

#Datetime modülünü içe aktarıp şu anki tarihi görüntüleyin.
import datetime

x = datetime.datetime.now()
print(x)

'''Python, sayılar üzerinde matematiksel görevler gerçekleştirmenize olanak tanıyan kapsamlı bir matematik modülü de dahil olmak üzere bir dizi yerleşik matematik işlevine sahiptir.'''

#Matematik işlemleri gerçekleştirme (min ve max)

x = min(5, 10, 25) #min() fonksiyonu ile en küçük değeri bulunur.
y = max(5, 10, 25) #max() fonksiyonu ile en büyük değeri bulunur.
print(x)
print(y)

x = abs(-7.25) #abs() fonksiyonu ile mutlak değeri bulunur.
print(x)

x = pow(4, 3) #pow() fonksiyonu ile 4'ün 3. kuvveti bulunur.
print(x)

#Matematik Modülü
import math

x = math.sqrt(64) #sqrt() fonksiyonu ile karekökü bulunur.
print(x)

#Örnek-1
import math

x = math.ceil(1.4) #ceil() fonksiyonu ile yukarı yuvarlama işlemi yapılır.
y = math.floor(1.4) #floor() fonksiyonu ile aşağı yuvarlama işlemi yapılır.
print(x) 
print(y) 

#Örnek-2
import math

x = math.pi #pi değeri bulunur.
print(x)
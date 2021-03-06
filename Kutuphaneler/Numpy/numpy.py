'''NumPy bir Python kütüphanesidir. NumPy dizilerle çalışmak için kullanılır. NumPy, "Sayısal Python"un kısaltmasıdır.'''
#Numpy Amacı:
#Python'da dizilerin amacına hizmet eden listelerimiz var, ancak işlenmesi yavaş.
#NumPy, geleneksel Python listelerinden 50 kata kadar daha hızlı bir dizi nesnesi sağlamayı amaçlar.

'''NumPy Neden Listelerden Daha Hızlı?'''
#NumPy dizileri, listelerin aksine bellekte tek bir sürekli yerde depolanır, böylece işlemler bunlara çok verimli bir şekilde erişebilir ve işleyebilir.
#Bu davranışa bilgisayar biliminde referans yeri denir.

'''NumPy'nin Kurulumu'''
#Bu komutu kullanarak yükleyin
'''C:\Users\Your Name>pip install numpy'''

import numpy 
arr = numpy.array([1, 2, 3, 4, 5])
print(arr) # [1 2 3 4 5]

#NumPy genellikle np takma adı altında içe aktarılır.
#Alias : Python'da takma ad, aynı şeye atıfta bulunmak için alternatif bir addır.
import numpy as np 

#Örnek-1       
import numpy as np 
arr = np.array([1, 2, 3, 4, 5]) 
print(arr) # [1 2 3 4 5]


#Numpy versiyonunu kontrol etme
import numpy as np
print(np.__version__) # 1.18.1

'''NumPy dizilerle çalışmak için kullanılır. 
NumPy'deki dizi nesnesine ndarray adı verilir. 
array() işlevini kullanarak bir NumPy ndarray nesnesi oluşturabiliriz.'''

#Tuple kullanılarak ndarray oluşturma
import numpy as np

array = np.array((1, 2, 3, 4, 5)) # Tuple
print(array)

#Dizilerdeki Boyutlar (İç içe diziler)





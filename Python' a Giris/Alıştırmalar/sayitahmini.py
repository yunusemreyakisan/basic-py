'''
1-100 arasında rastgele üretilecek bir sayyıyı aşağı yukarı ifadeleri ile
buldurmaya çalışın. (hak = 5)
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan olsun.  
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplayın.
'''

import random

sayi = random.randint(1, 100)  # 1-100 arasında rastgele sayı üret
can = int(input("kaç hak kullanmak istersiniz: "))
hak = 5
sayac = 0

while hak > 0:
    hak -= 1 # hak sayısını azalt
    tahmin = int(input('Tahmininizi giriniz: '))
    
    if sayi == tahmin: 
        print(f'Tebrikler bildiniz! {sayac} defada buldunuz. Toplam puanınız: {100 - (100/can) * (sayac-1)}') 
        break
    elif sayi > tahmin: 
        print('Yukarı')
    else: 
        print('Aşağı')
    
    if hak == 0:
        print('Hakkınız bitti! Tutulan sayi: ', sayi) # hak sayısı 0 olduğunda sayıyı yazdır.


# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 01:15:01 2019

@author: Asım
"""

print("""En Büyük Sayıyı Bulma Ve Sayıları Sıralama Programı
      

Çıkmak için 'q' tuşunu kullanabilirsiniz.


""")      

while True:
    num1 = input("Sayı 1 veya işlem : ")
    if num1 == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        num1 = float(num1)
        num2 = float(input("Sayi 2 : "))
        num3 = float(input("Sayi 3 : "))
        if num3 > num1 and num3 > num2:
            print("En büyük sayı : {}".format(num3))
        elif num2 > num1 and num2 > num3:
            print("En büyük sayı : {}".format(num2))
        elif num1 > num3 and num1 > num2:
            print("En büyük sayı : {}".format(num1))
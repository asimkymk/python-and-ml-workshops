# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""


print("""Negatif Pozitif Bulucu

Çıkmak için 'q' tuşuna basabilirsiniz.


""")
while True:
    value = input("Çıkış veya sayı : ")
    if value == "q":
        print("Çıkış yaplıyor...")
        break
    else:
        value = float(value)
        if value == 0:
            print("Girdiğiniz sayı 0!")
        elif value > 0:
            print("Girdiğiniz sayı 0'dan büyük POZİTİF sayıdır.")
        elif value < 0:
            print("Girdiğiniz sayı 0'dan küçük NEGATİF sayıdır.")
        else:
            print("HATALI İŞLEM!")
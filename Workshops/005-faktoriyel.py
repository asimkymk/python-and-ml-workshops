# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:34:39 2019

@author: Asım
"""

def faktoriyel(a):
    faktoriyelsonuc = 1
    for i in range(2,a+1):
        faktoriyelsonuc = faktoriyelsonuc * i
    return faktoriyelsonuc

print("""Faktöriyel Hesaplama
      
Çıkmak için 'q' tuşuna basınız!

""")

while True:
    islem = input("Sayı veya çıkış : ")
    if islem == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        sayi = int(islem)
        sayi = faktoriyel(sayi)
        print("{} ' nin faktöriyeli => {}".format(int(islem),sayi))
        print("*" * 15)
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:13:33 2019

@author: Asım
"""

#fonksiyonlar

def selamVer(isim = "ziyaretçi"):
    print("Merhaba " + isim)
    
selamVer("Asım")
selamVer("Mehmet")
selamVer("Mert")
selamVer("Metin")
selamVer()

def selamVer2(isim = "ziyaretçi", soyIsim = "arkadaş"):
    print("Merhaba " + isim + " "+ soyIsim)

selamVer2(isim = "Asım")
selamVer2(soyIsim = "Kaymak")
selamVer2("Asım","Kaymak")

#fonksiyonlarda return

#%%

def alanhesapla(a,b):
    return a * b / 2

sonuc = alanhesapla(5,8)
print(sonuc)
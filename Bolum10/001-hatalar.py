# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:22:44 2019

@author: Asım
"""


try:
    
    sayi = int(input("Sayı : "))
    print(sayi)
except ValueError:
    print("İşlem hatası integer değer alınamadı.")

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:51:27 2019

@author: Asım
"""

sayilar = [1,2,3,4,5]
sayilarKare = []

for sayi in sayilar:
    sayilarKare.append(sayi ** 2)

print(sayilarKare)

#mapping yöntemi ile yapma
sayilar = [1,2,3,4,5]

sayilarKaresi = list(map(lambda x: x ** 2,sayilar))
print(sayilarKaresi)




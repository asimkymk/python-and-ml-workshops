# -*- coding: utf-8 -*-

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30]) # 7 değer var

print(sayilar[5]) # 5. indexi verir yani  25

print(sayilar[0:3])# 0. indexten 3. indexe kadar 3 dahil değil

sayilar2 = np.array([[0,5,10],[15,20,25]])

print(sayilar2[0])
print(sayilar2[1])
print(sayilar2[1,2])
print(sayilar2[:,2]) # tüm satırlardan 2 numaralı indexleri verir
# : tüm elemanları kapsar
print(sayilar2[:,0:2])


print(sayilar2[-1,:-1])
print(sayilar2[:,-1])
print(sayilar2[0,::-1]) # ilk satırı ters çevirdik

testListe = np.round(10 * np.random.random((4,5)))
print(testListe)
print(testListe[:,0])
print(testListe[3,-1])
print(testListe[:,:2])
print(testListe[:,::-1])
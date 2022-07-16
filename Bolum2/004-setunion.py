# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}
#birleşimkümesi
print(setA | setB)  #yol1

print(setA.union(setB))#yol2

#kesişim kümesi

print(setA & setB) #yol1

print(setA.intersection(setB)) #yol2

#fark kümesi

print(setA - setB) # A nın B den farkı yol1
print(setB-setA) # B nin A dan farkı yol1

print(setA.difference(setB))# A nın B den farkı yol2
print(setB.difference(setA)) # B nin A dan farkı yol2

#birleşim-kesişim kümesi (simetrik fark)
print(setA ^ setB) #yol1
print(setA.symmetric_difference(setB)) #yol2
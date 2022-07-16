# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:56:30 2019

@author: Asım
"""

sayilar = [1,2,3,4,5]

sayilarKare = list(map(lambda x : x ** 2,sayilar))

sayilarFilter = list(filter(lambda x: x > 2,sayilar))

print(sayilarKare)
print(sayilarFilter)
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:00:31 2019

@author: Asım
"""
#reduce modülü import edilmeli

from functools import reduce as rd

sayilar = [1,2,3,4,5]

sayilarMap = list(map(lambda x: x ** 2,sayilar))

sayilarFilter = list(filter(lambda x: x>2, sayilar))

sayilarReduce = rd(lambda x,y: x * y,sayilar)

print(sayilarReduce)
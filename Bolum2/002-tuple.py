# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""

#listelerden tek farkı elemanları değiştirilemez

mytuple = ()

mytuple = (1,2,3,4,5)

mytuple = ("Asım",12,3,21,("Asım",1))

#tuplelar

tuplevalues = (1,2,3,4,5,"Ankara","İstanbul",25)

print(tuplevalues)
print(len(tuplevalues))
print(tuplevalues[5])
#↓tuplelarda eleman değiştirilemez
#tuplevalues[5] = "Bayburt"
#print(tuplevalues)    kod hata verir


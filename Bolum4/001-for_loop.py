# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:03:28 2019

@author: Asım
"""
#for döngüsü
cities = ["Ankara","İstanbul","İzmir"]
print(cities[0])
print(cities[1])
print(cities[2])
for city in cities:
    if city == "Ankara":
        print("ok")
    
    print(city + " için kod = " + city[0:3])
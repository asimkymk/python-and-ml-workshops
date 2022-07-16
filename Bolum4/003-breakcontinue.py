# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:03:28 2019

@author: Asım
"""
#☺break continue
cities = ["Ankara","İstanbul","İzmir"]
print(cities[0])
print(cities[1])
print(cities[2])
for city in cities:
    if city == "İstanbul":
        continue
    
    print(city + " için kod = " + city[0:3])
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""

#listelerle çalışmak
#boş liste

mylist = []

#integer liste

mylist1 = [1,2,3,4,5,6]

#stringliste

mylist2 = ["Asım","Mehmet","Fatih"]

#mix list
mylist3 = [19,123,"Asım",12,"Mehmet"]

#liste içinde liste

mylist4 = [12,[2,"Asım","Merhaba"],[[1,2,3],1,2,3]]

#listeler
students = ["Asım","Mehmet","Salih"]
print(students)
print(students[1])

#ekleme
students.append("Temel")
print(students)

#silme
students.remove("Mehmet")
print(students)

#veri değişme
students[1] = "Ahmet"
print(students)

#eleman sayma
print(len(students))

#istediğin indexe ekleme  silmeden
students.insert(2, "Enes")
print(students)

#liste oluşturma yöntem 2
cities = list(("İstanbul","Ankara","Eskişehir","Bayburt"))
print(cities)

#liste temizleme
cities.clear()
print(cities)

cities = list(("İstanbul","Ankara","Bayburt","Eskişehir","Bayburt"))

#listedeki eleman sayısı

print(cities.count("Eskişehir")) # eskişehirden bir tane var
print(cities.count("Bayburt")) #bayburttan iki tane var 

#eleman kaçıncı indexte?

print(cities.index("Ankara")) #1. indexte

#index numarasından eleman silme

cities.pop(0) # 0. indexteki elemanı siler
print(cities)

#listeyi çevirme
cities.reverse() # listeyi ters çevirir
print(cities)

# sıralama
#küçükten büyüğe
cities.sort()
print(cities)
#büyükten küçüğe
cities.sort(reverse=True)
print(cities)

cities2 = ["İzmir","Diyarbakır","Adana","Mersin"]
print(cities)
print(cities2)

#listenin elemeanlarını diğer listeye ekleme
cities.extend(cities2)
print(cities)















# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:56:14 2019

@author: Asım
"""

#stringlerde çalışmak

#substring

message = "Hello World"

print(message)
print(message[2:5]) # 2. karakterden 5. karaktere kadar 5 dahil değil ilk karakter = 0
print(message[::-1]) #tersten yazar
print(message[:3:2])

#len fonksiyonu
#karakter sayısını ölçer

print(len(message))
#metnin son karakterini öğrenmek için yollar:
#yol-1
print(message[len(message)-1])
#yol-2
new_message = message[::-1]
print(new_message[0])

#lower ve upper fonksiyonları
#texti tamamen küçültür = lower
#texti tamamen büyültür= upper

first_string = "PytHoN oGREniyORUm"
second_string = "pYThoN oGREniyOruM"
print(first_string.upper())
print(first_string.lower())
print(second_string.lower())
if (first_string.lower() == second_string.lower()):
    print("Tamam")
else:
    print("Hata")
#replace fonksiyonu
    #karakter değiştirme

print(message)
print(message.replace("o","a"))


#split ve strip

information = "ASIM KAYMAK 19 BAYBURT"
print(information.split(" "))
print(information.split())
information1 = "ASIM;KAYMAK;19;BAYBURT"
print(information1.split(";"))

information3= "                 ASIM KAYMAK 19 BAYBURT                   "
print(information3.strip())#sağ ve soldaki boşlukları siler
print(information3.rstrip())#sağdaki boşlukları siler
print(information3.lstrip()) #soldaki boşlukları siler
print(information3.strip().split())



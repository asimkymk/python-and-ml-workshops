# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:02:20 2019

@author: Asım
"""

#dosyaokuma işlemleri
#dosya okuma kipi 'r'
#eğer dizinde o dosya yoksa hata verir varsa o dosyayı açar

file = open("bilgiler.txt","r",encoding="utf-8")


for i in file: #listeler gibi dosyanın her bir satırında geziyoruz
    print(i) # iki satır atıyor

file1 = open("bilgiler.txt","r",encoding="utf-8")
for a in file1:
    print(a,end="") #sadece bir satır atlıyor.
file1.close()

#read fonksiyonu
file2 = open("bilgiler.txt","r",encoding="utf-8")
reader = file2.read()
print("Txt Dosyası :\n",reader,sep="")#en başta readerı yazarken bir karakter fazladan başlıyor onu siliyoruz
file2.close()

#readline fonksiyonu

file3 = open("bilgiler.txt","r",encoding="utf-8")
print(file3.readline())#1.satırı okudu
print(file3.readline()) #ikinci satırı okudu
print(file3.readline()) # üçüncü satırı okudu
print(file3.readline()) #4.satırı okudu
print(file3.readline()) # beşinci satırı okdudu
file3.close()

#readlines fonksiyonu
file4 = open("bilgiler.txt","r",encoding="utf-8")
hersatirbirstringliste = file4.readlines()
print(hersatirbirstringliste)
file4.close()
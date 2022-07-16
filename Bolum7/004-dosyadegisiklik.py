# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:05:10 2019

@author: Asım
"""

#dosyalarda değişiklik yapma işlemleri
#r+ kipi hem okuma hem yazma yapabiliyor
with open("bilgiler.txt","r+",encoding="utf-8") as file1:
    print(file1.read())
    file1.seek(11) #12. karakterin olduğu yere gittik
    file1.write("Deneme") #dosyanın üzerine yazıyor
    file1.seek(0)
    print(file1.read())
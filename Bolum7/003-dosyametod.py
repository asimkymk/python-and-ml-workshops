# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:02:48 2019

@author: Asım
"""

#dosyalarda kullanılan metodlar
#dosyaları sürekli kapatmayla uğraşmamak için otomatik kapatma fonksiyonu = with open

with open("bilgiler.txt","r",encoding="utf-8") as file1:
    for i in file1:
        print(i)

#tell() fonksiyonu imlecin kaçıncı karakterde(baytta) olduğunu söyler
#seek() fonksiyonu imleci yazdığımızkaraktere(bayta) götürür
with open("bilgiler.txt","r",encoding="utf-8") as file2:
    print(file2.tell())
    file2.seek(20)
    print(file2.tell()) #imleci 20. karakterin olduğu yere götürdük
    a = file2.read(10) #imlecin olduğu yerden 10 karakter okuduk
    print(a)
    b= file2.read()
    print(b)
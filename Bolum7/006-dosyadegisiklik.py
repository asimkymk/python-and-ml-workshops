# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:06:03 2019

@author: Asım
"""

#dosyanın ortasında değişiklik yapmak
#liste yöntemi ile
with open("bilgiler.txt","r+",encoding="utf-8") as file1:
    satirliste = file1.readlines()
    print(satirliste)
    #eklemek istediğimiz satırı seçiyoruz listeden
    satirliste[2] = "Furkan Tay\n" + satirliste[2] # yöntem 1
    satirliste.insert(5,"Serhat Buldur \n")
    print(satirliste)
    file1.seek(0)
    for i in satirliste: #for yerine file1.writelines(satirliste) diyeibliriz
        file1.write(i)
with open("bilgiler.txt","r+",encoding="utf-8") as file2:
    print(file2.read())
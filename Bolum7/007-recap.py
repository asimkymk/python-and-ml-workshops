# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:06:18 2019

@author: Asım
"""

#not hesplama
def nothesapla(satır):
    satır = satır[:-1] #\n silindi
    #split fonksiyonu
    liste = satır.split(",")
    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])
    puan = (vize1 * 30 + vize2 * 30 + final * 40) / 100
    harfnotu = ""
    if puan>=90:
        harfnotu = "AA"
    elif puan >=85:
        harfnotu = "BA"
    elif puan>=80:
        harfnotu = "BB"
    elif puan>=75:
        harfnotu = "CB"
    elif puan>=70:
        harfnotu = "CC"
    elif puan>=65:
        harfnotu ="DC"
    elif puan>=60:
        harfnotu = "DD"
    elif puan >=55:
        harfnotu = "FD"
    elif puan >=50:
        harfnotu = "FF"
    elif puan <50:
        harfnotu = "DERS TEKRARI"

    return "{} -----------------> {}\n".format(isim,harfnotu)




with open("dosya.txt","r+",encoding="utf-8") as  file1:
    ekleneceklerlistesi = []
    for i in file1:
        ekleneceklerlistesi.append(nothesapla(i))
    print(ekleneceklerlistesi)
    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in ekleneceklerlistesi:
            file2.write(i)
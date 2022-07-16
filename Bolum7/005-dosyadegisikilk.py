# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:05:31 2019

@author: Asım
"""

#değişiklik
#alt satıra geçip yazı yazma
with open("bilgiler.txt","a",encoding="utf-8") as file1:
    file1.write("Mehmet Türkan\n")
with open("bilgiler.txt","r+",encoding="utf-8") as file2:
    print(file2.read())

#dosyanın başında değişiklik yapma
with open("bilgiler.txt","r+",encoding="utf-8") as file3:
    icerik = file3.read()
    icerik = "Ataberk Karadağlı\n" + icerik
    print(icerik)
    file3.seek(0)
    file3.write(icerik)
    print(file3.read())
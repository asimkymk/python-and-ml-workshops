# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 00:53:36 2019

@author: Asım
"""

print("""Asal Sayı Programı
      
1- Belli Aralıktaki Asal Sayıları Bul

2- Sayı Sorgula


Çıkmak için 'q' tuşuna basınız!
""")

while True:
    prog = input("İşlem seçiniz : ")
    if prog == "q":
        print("Çıkış yapılıyor...")
        break
    elif prog == "1":
        firstnumber = int(input("İlk değeri girin : "))
        secondnumber = int(input("İkinci değeri girin : "))
        if firstnumber >= secondnumber or firstnumber <= 0 or secondnumber <= 0:
            print("Hatalı değer aralığı girdiniz.")
            break
        else:
           
            for i in range(firstnumber,secondnumber+1):
                if i == 1:
                    continue
                asalmi = True
                for a in range(2,i):
                    if i % a == 0:
                        asalmi = False
                        break
                if asalmi == True:
                    print(i, " sayısı asal sayıdır.")
                    print("*"*20)
    elif prog == "2":
        value = int(input("Sorgulamak istediğiniz sayıyı girin : "))
        asalmi = True
        for a in range(2,value):
            if value % a==0:
                asalmi = False
                break
        if asalmi:
            print(value, " sayısı asal sayıdır.")
            print("*"*20)
    
                            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
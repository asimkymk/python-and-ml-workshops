# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 23:09:56 2019

@author: Asım
"""

liste = ["Asım",0,2,12,"Test",12.3,"12"]


for i in liste:
    print("Değer : " + str(i))
    try:
        
        print(1/ i)
    except TypeError:
        print("Tip hatası! Girdi, integer değer değil!")
    except ZeroDivisionError:
        print("İşlem Hatası! Bölen 0 olamaz.")
    except:
        print("Bilinmeyen hata.")
    finally:
        print("İşlemler tamamlandı!")
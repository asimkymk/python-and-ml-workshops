# -*- coding: utf-8 -*-
import data
import time as tm
urunUI = data.productSettings()
markaUI = data.brandsSettings()

def AnaMenu():
    print("""ANA MENÜ
      
      1 - MARKA İŞLEMLERİ
      
      2 - ÜRÜN İŞLEMLERİ
      
      3 - SEPET İŞLEMLERİ
      
      4 - ÇIKIŞ
      """)
    while True:
            
        anaMenuIslem = input("İşlem : ")
        if anaMenuIslem == "4":
            print("Çıkış yapılıyor...")
            urunUI.connectionClose()
            markaUI.connectionClose()
            print("Çıkışlar yapıldı.")
            return
            
        elif anaMenuIslem == "3":
            SepetMenu()
            return
        elif anaMenuIslem == "2":
            UrunMenu()
            return
        elif anaMenuIslem == "1":
            MarkaMenu()
            return

def MarkaMenu():
    print("""MARKA İŞLEMLERİ
          
              A - MARKA EKLE
              
              B - MARKA LİSTE
              
              C - MARKA SORGU
              
              D - MARKA SİL
              
              E - ANA MENÜ
              """)
    while True:
        markaMenuIslem = input("İşlem : ")
        if markaMenuIslem.lower() == "e":
            AnaMenu()
            return
        elif markaMenuIslem.lower() == "a":
            markaad = input("Eklenecek Marka İsmi : ")
            markaUI.brandAdd(markaad)
            tm.sleep(3.5)
            MarkaMenu()
            return
        elif markaMenuIslem.lower() == "b":
            
            markaUI.brandList()
            tm.sleep(3.5)
            MarkaMenu()
            return
        elif markaMenuIslem.lower() == "c":
            name = input("Marka İsmi : ")
            markaUI.brandSearch(name)
            tm.sleep(2)
            MarkaMenu()
            return
        elif markaMenuIslem.lower()=="d":
            name = input("Marka İsmi : ")
            markaUI.brandDelete(name)
            tm.sleep(1)
            MarkaMenu()
            return
def UrunMenu():
    
    print("""ÜRÜN İŞLEMLERİ
          
              A - ÜRÜN EKLE
              
              B - ÜRÜN LİSTE
              
              C - ÜRÜN SORGU
              
              D - ÜRÜN SİL
              
              E - ANA MENÜ
              """)
    while True:
        urunMenuIslem = input("İşlem : ")
        if urunMenuIslem.lower() == "e":
            AnaMenu()
            return
        elif urunMenuIslem.lower() == "a":
            productName = input("Ürün İsmi : ")
            rate0 = int(input("0 Puan : "))
            rate1 = int(input("1 Puan : "))
            rate2 = int(input("2 Puan : "))
            rate3 = int(input("3 Puan : "))
            rate4 = int(input("4 Puan : "))
            rate5 = int(input("5 Puan : "))
            brandName = input("Marka İsmi : ")
            urunUI.productAdd(productName,rate0,rate1,rate2,rate3,rate4,rate5,brandName)
            tm.sleep(3.5)
            UrunMenu()
            return
        elif urunMenuIslem.lower() == "b":
            urunUI.productList()
            tm.sleep(4)
            UrunMenu()
            return
        elif urunMenuIslem.lower() == "c":
            name = input("Ürün Adı : ")
            urunUI.productQuery(name)
            tm.sleep(3.5)
            UrunMenu()
            return
        elif urunMenuIslem.lower() == "d":
            name = input("Ürün İsmi : ")
            urunUI.productDelete(name)
            tm.sleep(3.5)
            UrunMenu()
            return
def SepetMenu():
    print("""SEPET İŞLEMLERİ
          
              A - SEPETE EKLE
              
              B - SEPETTEN ÇIKAR
              
              C - SATIN AL
              
              D - ANA MENÜ
              """)
    while True:
            
        sepetmenuIslem = input("İşlem : ")
        if sepetmenuIslem.lower() == "d":
            print("Ana Menüye geçiş yapılıyor.")
            AnaMenu()
            return
AnaMenu()
    
    
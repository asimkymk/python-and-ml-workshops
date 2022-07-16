# -*- coding: utf-8 -*-
import hesapMakinesiModule as hesap
print("""
İşlemler :

1 - Topla

2 - Çıkar

3 - Çarp

4 - Böl

5 - Faktöriyel      

q - Çıkış""")
    
while True:
    a = input("İşlem numarası : ")
    if a == "q":
        print("Çıkış yapılıyor...")
        break
    elif a == "1":
        sayi1 = int(input("Sayı 1 :"))
        sayi2 = int(input("Sayı 2 :"))
        print(hesap.topla(sayi1,sayi2))
    elif a == "2":
        sayi1 = int(input("Sayı 1 :"))
        sayi2 = int(input("Sayı 2 :"))
        print(hesap.cikar(sayi1,sayi2))
    elif a == "3":
        sayi1 = int(input("Sayı 1 :"))
        sayi2 = int(input("Sayı 2 :"))
        print(hesap.carp(sayi1,sayi2))
    elif a == "4":
        sayi1 = int(input("Sayı 1 :"))
        sayi2 = int(input("Sayı 2 :"))
        print(hesap.bol(sayi1,sayi2))
    elif a == "5":
        sayi1 = int(input("Sayı :"))
        print(hesap.faktoriyel(sayi1))
    else:
        print("Hatalı işlem numarası. Lütfen tekrar deneyin!")
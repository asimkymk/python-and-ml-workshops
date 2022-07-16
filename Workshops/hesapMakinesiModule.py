# -*- coding: utf-8 -*-

def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1, sayi2):
    return sayi1- sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2

def faktoriyel(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc = sonuc * i
    return sonuc
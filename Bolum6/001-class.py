# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:21:48 2019

@author: Asım
"""

class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1-sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik()

print(matematik.topla(5,10))
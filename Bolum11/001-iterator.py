# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:13:08 2019

@author: Asım
"""

#iterator oluşturmak
#iter metodu

liste = [1,2,3,4,5]


iterator = iter(liste)

print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in liste:
    print(i)
    
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
class Kumanda():
    def __init__(self,kanalListesi):
        self.kanalListesi = kanalListesi
        self.index = -1
            
    def __iter__(self,):
        return self
    def __next__(self,):
        self.index += 1
        if self.index < len(self.kanalListesi):
            return self.kanalListesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda = Kumanda(["Atv","Kanald","TRT","ShowTv","Fox"])

iterator = iter(kumanda)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
        
        
        
        
        
        
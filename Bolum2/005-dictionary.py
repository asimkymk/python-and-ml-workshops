# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""
#sözlükler 
#sırasız veri tutarlar
#anahtar-değer (key-value) ilişkisi vardır
mydic = {"bir":1,"iki":2}
print(mydic)
#yazım kolaylığı


treng_dict = {
        "book" : "kitap",
        "table" : "masa"
        
        }

print(treng_dict)

print(treng_dict["table"])
print(treng_dict["book"])

#eleman değiştirme

treng_dict["table"] = "Masa 1"
print(treng_dict)

#eleman ekleme

treng_dict["pencil"] = "Kalem"
print(treng_dict)

#sozluk oluşturmanın diğer yolu 

sozluk2 = dict(kitap = "book",kalem="Pencil")
print(sozluk2)
#eleman silme
del(sozluk2["kitap"])
print(sozluk2)








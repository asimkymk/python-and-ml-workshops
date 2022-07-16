# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""

#kümeler
#indexleri yoktur elemanların sıraları yoktur
#veri tekrarı söz konusu olamaz kümelerdeki gibi tek bir eleman olabilir.
myset = {1,2,3}
myset= {"Engin","Asım","Mehmet","Berkay"}
print(myset) #sırası karışık gelir

for i in myset:
    print(i)

print("Asım" in myset) #setin içinde olduğu için true döner

print("Mahmut" in myset) # setin içinde olmadığı için false döner

if ("Asım" in myset):
    print("Asım ismi var.")
if ("Mahmut" in myset):
    print("Mahmut ismi var.")
else:
    print("Mahmut ismi yok.")
    
#eleman ekleme
myset.add("Fırat")
print(myset)

myset.update(["Merve","Ceren"])
print(myset)

print(len(myset))

myset.remove("Merve") # eğer bu isim yoksa hata verir varsa siler
print(myset)

myset.discard("Mahmut") # bulamazsa hata vermez bulursa siler


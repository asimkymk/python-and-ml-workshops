# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:27:48 2019

@author: Asım
"""

#dosya açma ve dosya okuma
#dosya açmak için open fonksiyonu kullanılır
#open(dosya_adi, dosya_erisim_kipi)
#w dosya kipi: dizinde dosya oluşturur ve içine yazıyı yazar. aynı dosyadan varsa silip tekrar oluşturur

open("bilgiler.txt", "w")
file = open("bilgiler.txt","w") # artık tüm işlermlerimizi file dan yapabiliyoruz
file.close() #dosyayı kapadık
#istediğmiz klasöre kaydetme
file1 = open("C:/Users/Asım/Desktop/bilgiler.txt","w")
file1.close()

file2 = open("bilgiler.txt","w",encoding="utf-8") # türkçe karakterler için utf-8 kullanıyoruz. en genel encode.
file2.write("Asım Kaymak Fenerbahçeli Ğ İ")
file2.close()

#a kipi dosyaya ekleme yapar dosa yoksa oluşturur

file3 = open("bilgiler.txt","a",encoding="utf-8")
file3.write("Ahmet Gürsel Gürleyen")
file3.close()
file4 = open("bilgiler.txt","a",encoding="utf-8")
file4.write("\nDeneme\nHmmm\nTest")
file4.close()
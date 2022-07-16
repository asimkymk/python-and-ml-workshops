# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
#column larını düzenliyoruz isteğimize göre
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar["İsim"])

print(notlar.loc[:,"İsim"]) # tüm isimleri verir
print("*"*10)
print(notlar.loc[:5,"İsim"]) # 0 dan 5. indexe kadar verir 5 dahil
print("*"*10)
print(notlar.loc[:5,"İsim":"Test4"]) # ilk 5i test4 e kadar olan değerleri verir
print("*"*10)
print(notlar.loc[:5,["İsim","Soyisim","Final"]])
print("*"*10)
print(notlar.loc[:5,:"Test2"])
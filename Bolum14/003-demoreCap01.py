# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
#column larını düzenliyoruz isteğimize göre
notlar.columns = ["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar["İsim"])
print(notlar.iloc[2]) #2 index numaralı kişinin bilgilerini döker.
print(notlar[1:5]) #1 den 5. index numaları değere kadar gider 5 dahil değil
print(notlar[0:10])
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df = pd.DataFrame()
print(df)
print("*"*10)
data2 = [10,20,30,40,50]
df2 = pd.DataFrame(data)
print(df2)

print("*"*10)

data3 = [["Engin",33,"Ankara"],["Derin",4,"Ankara"],["Salih",32,"İstanbul"]]
df3 = pd.DataFrame(data3,columns = ["İsim","Yas","Şehir"],index = [1,2,3])
print(df3)

print("*"*10)

data4 = {"İsim":["Engin","Derin","Salih"],"Yas":[33,4,32],"Şehir":["Ankara","Ankara","İstanbul"]}
df4 = pd.DataFrame(data3,columns = ["İsim","Yas","Şehir"],index=[1,2,3])
print(df4)
print(df4["Yas"])
print(df4.loc[2]) #atanan index numarasına göre yazar
print(df4.iloc[1]) #normal index numarasına göre yazar
print("*"*10)

#del(df4["Şehir"]) bununla silebiliriz
df4.pop("Şehir") # bununla da silebiliriz.
print(df4)

print("*"*10)

df5 = df4.append(df3)
print(df5)
print(df5.head())#ilk 5 datayı verir
print(df5.tail()) #son 5 datayı verir.

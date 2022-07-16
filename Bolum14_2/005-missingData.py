# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from numpy.random import randn

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
print(arr)

df = pd.DataFrame(arr,index = ["Index1","Index2","Index3"],columns = ["Column1","Column2","Column3"])
print(df)

print(df.dropna()) 
print(df.dropna(axis = 1))
print(df.dropna(thresh = 2)) #2 tane doğru veri varsa silmez
print(df)

print(df.fillna(value = 1)) # na ları 1 ile doldurur

print(df.sum().sum())  # verilerin toplamı

print(df.size) # kaç veri var onu söyler
print(df.isnull().sum().sum()) #boş olanları toplar

def CalculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

print(df.fillna(value = CalculateMean(df)))





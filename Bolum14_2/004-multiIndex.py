# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]

innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]

zipList = list(zip(outerIndex,innerIndex))
print(zipList)

zipList = pd.MultiIndex.from_tuples(zipList)
print(zipList)

df = pd.DataFrame(randn(9,3),zipList,columns = ["Column1","Column2","Column3"])
print(df)

print(df["Column1"])

print("*"*10)
print(df.loc["Group1"])
print(df.loc[["Group1","Group2"]])
print("*"*10)
print(df.loc["Group1","Index1"])
print(df.loc["Group1","Index1"]["Column1"])
print("*"*10)
print(df.loc["Group1"].loc["Index1"])
print(df.loc["Group1"].loc["Index1"]["Column1"])
print("*"*10)
print(df.index.names)
df.index.names = ["Groups","Indexes"]
print(df)
print(df.xs("Group1"))
print(df.xs("Group1").xs("Index1").xs("Column1"))
print("*"*10)
print(df.xs("Index1",level = "Indexes"))
print("*"*10)



















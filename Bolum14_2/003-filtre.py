# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])
print(df)
print("*"*10)
print(df > -1)
print("*"*10)
booleanDf = df > -1
print(booleanDf)
print("*"*10)
print(df[booleanDf])
print("*"*10)
print(df[df > -1])
print("*"*10)
print(df)
print(df["Column1"])
print("*"*10)
print(df["Column1"] > -1)
print("*"*10)
print(df[df["Column1"] > -1])
print("*"*10)
print(df["Column1"] > 0.5)
print("*"*10)
print(df[df["Column1"] > 0.5])
print("*"*10)
print((df["Column1"] > 0.5) & (df["Column2"] < 0))
print(df[(df["Column1"] > 0.5) & (df["Column2"] < 0)])
print("*"*10)
print(df[(df["Column1"] > 0.5) | (df["Column2"] < 0)])
print("*"*10)
print(df)
print("*"*10)
df["Column4"] = pd.Series(randn(4),["A","B","C","D"])
print(df)
print("*"*10)
df["Column5"] = randn(4)
print(df)
print("*"*10)
df["Column6"] = ["newValue1","newValue2","newValue3","newValue3"]
print(df)
print("*"*10)
df = df.set_index("Column6")
print(df)
print("*"*10)
print(df.index.names)
print("*"*10)
print(df.columns)
print("*"*10)
print(df.shape)
print(df.head())
print(df.tail())













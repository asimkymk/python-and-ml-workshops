# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df = pd.DataFrame(data = np.random.randn(3,3),index = ["a","b","c"],columns = ["Column1","Column2","Column3"] )
print(df)
print("*"*10)
print(df["Column1"])
print("*"*10)
print(type(df["Column1"]))
print("*"*10)
print(df.loc["a"])
print(type(df.loc["a"]))
print("*"*10)
print(df[["Column1","Column2"]])
print(df[["Column1","Column2"]].iloc[:1])
print("*"*10)
df["Column5"] = df["Column1"] + df["Column2"] + df["Column3"]
print(df)
print("*"*10)
print(df.drop("Column5",axis = 1))
print(df)
print(df.drop("Column5",axis = 1,inplace= True))
print("*"*10)
print(df)
print("*"*10)
print(df.loc["a"])
print(df.iloc[0])
print("*"*10)
print(df.loc["a"]["Column1"])
print(df["Column1"].loc["a"])
print("*"*10)
print(df.loc[["a","b"],["Column1","Column2"]])

              
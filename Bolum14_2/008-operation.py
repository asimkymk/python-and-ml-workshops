# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})
print(df)
print(df.head(3))


print(df["Column2"].unique())

print(df["Column2"].value_counts())

print(df[(df["Column1"] >= 4) & (df["Column2"] ==300)])

print(df)

df["Column2"] = 3 * df["Column2"]
print(df)

def times3(z):
    return 3 * z

print(df["Column2"].apply(times3))


print(df["Column2"].apply(lambda x: x * 3))

print(df["Column3"].apply(len))

print(df.drop("Column3",axis = 1,inplace = True))

print(df.columns)
print(df.index)
print(len(df.index))
print(df.index.names)
print(df)

print(df.sort_values("Column2")) # küçükten büyüğe

print(df.sort_values("Column2",ascending = False)) # büyükten küçüğe

df = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})
    
print(df)

print(df.pivot_table(index = "Ay",columns = "Şehir",values="Nem"))


print(df.pivot_table(index = "Şehir",columns = "Ay",values="Nem"))





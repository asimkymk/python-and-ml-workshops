# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#%%
df = pd.read_csv("USvideos.csv")
print(df)
print(df.columns)

newDataset1  = df.drop(["video_id","trending_date"],axis = 1)
print(newDataset1)

newDataset1.to_csv("new.csv")
newDataset1.to_csv("new.csv",index = False)

#%%

excelset = pd.read_excel("excelfile.xlsx")
print(excelset)
excelset["Column5"] = ["Asım","Kaymak","IUC","Bilgisayar"]
print(excelset)
excelset.to_excel("newexcel.xlsx")

#%%

new = pd.read_html("http://www.contextures.com/xlSampleData01.html",header = 0)
print(new)

print(len(new))
print(new[0])



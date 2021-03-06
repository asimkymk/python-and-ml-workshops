# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

dataset = {
            "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
            "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
           "Maaş":[3000,3500,2500,4500,4000,2000]
            }
df = pd.DataFrame(dataset)
print(df)
DepGroup = df.groupby("Departman")
print(DepGroup)
print(DepGroup.sum())
print(df.groupby("Departman").sum())
print(DepGroup.sum().loc["Bilişim"])
print(int(DepGroup.sum().loc["Bilişim"]))
print(df.groupby("Departman").count())
print(df.groupby("Departman").max())
print(df.groupby("Departman").min())
print(df.groupby("Departman").min()["Maaş"])
print(df.groupby("Departman").min()["Maaş"]["Bilişim"])
print(df.groupby("Departman").mean())
print(df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"])

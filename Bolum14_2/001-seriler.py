# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

labelsList = ["Mustafa","Kemal","Asım","Kadir","Zeynep"]
dataListe = [10,20,30,40,50]

print(pd.Series(data = dataListe, index = labelsList))

print(pd.Series(dataListe,labelsList))

print(pd.Series(dataListe))

npArray = np.array([10,20,30,40,50])
print(pd.Series(npArray,labelsList))


print(pd.Series(data = npArray,index=["A","B","C","D","E"]))


dataDict = {"Kadir":30,"Kemal":80,"Kamuran":60}

print(pd.Series(dataDict))

ser2017 = pd.Series([5,10,14,20],["Buğday","Mısır","Kiraz","Erik"])
print(ser2017)

ser2018 = pd.Series([2,12,12,6],["Buğday","Mısır","Çilek","Erik"])
print(ser2018)

print(ser2017+ser2018)

total = ser2017 + ser2018
print(total)
print(total["Erik"])
print(total["Çilek"])


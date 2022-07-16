# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:24:34 2019

@author: Asım
"""

import pandas as pd
import numpy as np



data = np.array(["Engin","Derin","Salih"])
s = pd.Series(data, index=[1,2,3]) #index yazmak zorunlu değil
print(s)
print("*"*10)
data2 = {"matematik":10,"fizik":20,"beden eğitimi":100}
s2 = pd.Series(data2,index=["fizik","matematik","beden eğitimi"])#index yazmak zorunlu değil yerleri değiştirdik
print(s2)
print(s2[0]) # index yerlerini değiştirdiğimiz için ilk önce fiziği yazdı
print(s2["beden eğitimi"])
print("*"*10)


s3 = pd.Series(5,index=[2])
print(s3)


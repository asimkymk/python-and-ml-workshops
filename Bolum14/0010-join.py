# -*- coding: utf-8 -*-

import pandas as pd
data1 = {
            "id":[1,2,3,4],
            "ad":["Asım","Engin","Derin","Salih"],
            "soyad":["Kaymak","Demiroğ","Demiroğ","Kaya"]
        }

data2 = {
            "id":[1,3,4,7],
            "ad":["Ayşe","Ahmet","Ali","Cemal"],
            "soyad":["Kaymak","Demiroğ","Demiroğ","Kaya"]
        }

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)
print(data1Df)
print(data2Df)


print(pd.merge(data1Df,data2Df,on="id",how="inner")) # id si aynı olanları birleştirdi

print(pd.merge(data1Df,data2Df,on="id",how="left")) # solda olup sağda olmayanları getirdi dahil etti

print(pd.merge(data1Df,data2Df,on="id",how="right")) # tam tersi


print(pd.concat([data1Df,data2Df],axis = 1))

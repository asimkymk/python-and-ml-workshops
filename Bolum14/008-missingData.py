# -*- coding: utf-8 -*-

import pandas as pd

ufoReps = pd.read_csv("ufo.csv")
print(ufoReps.columns)
print(ufoReps.loc[:50,][["City","Colors Reported"]])

print(ufoReps.isnull()) # boş olan datalara True olmayanlar False yazar

print(ufoReps.notnull()) # isnull un tam tersi

print(ufoReps.isnull().sum()) # boş olanların sayısı her bir sütundaki

print(ufoReps[ufoReps.City.isnull()]) #şehirlerde boş olanları gösterir
print(ufoReps.shape) # kaç data olduğunu söyler

ufoReps["Shape Reported"].fillna(value="Belirsiz",inplace=True) #  shapre reportedda boş olanları belirsiz yaptık
print(ufoReps["Shape Reported"].value_counts(dropna="False")) #dropna yaparak shapre rportedda kaç tane dolu data olduğunu gösterdik


ufoReps = ufoReps.dropna(how="all") # tüm hepsi boş olanları siler
print(ufoReps.shape)

ufoReps = ufoReps.dropna(subset=["City","Colors Reported"], how = "all")
#city ve color rported column larından how = all diyerek ikisinin de boş olduklarını sildik any deseydik herhangi birinin boş olması yeterli olacaktı

print(ufoReps.shape)


ufoReps =ufoReps.dropna(how = "any") # en az 1 boş data bulunan verileri kaldırdık
print(ufoReps.shape) #hepsi dolu


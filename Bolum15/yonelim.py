# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("yonelimfinal.csv")

print(data.columns)

def bolgeCevirici(x):
    if x == "Akdeniz":
        return 1
    elif x == "Doğu Anadolu":
        return 2
    elif x == "Ege":
        return 3
    elif x == "Güneydoğu":
        return 4
    elif x == "Karadeniz":
        return 5
    elif x == "Marmara":
        return 6
    elif x == "İç Anadolu":
        return 7

def egitimCevirici(x):
    if x == "İlkokul":
        return 1
    elif x == "Ön Lisans":
        return 2
    elif x == "Ortaokul":
        return 3
    elif x == "Lise":
        return 4
    elif x == "Lisans Üstü":
        return 5
    elif x == "Lisans":
        return 6
    
def yasCevirici(x):
    if x == "0-18":
        return 1
    elif x == "18-30":
        return 2
    elif x == "30-50":
        return 3
    elif x == "50-60":
        return 4
    elif x == "60+":
        return 5

def partiÇevirici(x):
    if x == "AKP":
        return 1
    elif x == "CHP":
        return 2
    elif x == "DIĞER":
        return 3
    elif x == "HDP":
        return 4
    elif x == "IYI PARTI":
        return 5
    elif x == "MHP":
        return 6
data["bolgeNum"] = data["Bolge"].apply(bolgeCevirici)
data["egitimNum"] = data["Egitim"].apply(egitimCevirici)
data["yasNum"] = data["Yas"].apply(yasCevirici)
data["partiNum"] = data["parti"].apply(partiÇevirici)

yParti = data.iloc[:,-1].values.reshape(-1,1)
xBolgeEgitimYas = data.iloc[:,[16,17,18]].values
xYas = data.yasNum.values.reshape(-1,1)
regressionPoly = PolynomialFeatures(degree = 10)
regression = LinearRegression()

xPoly = regressionPoly.fit_transform(xBolgeEgitimYas)

regression.fit(xPoly,yParti)
#plt.scatter(data.yasNum,data.partiNum,color = "red")
#plt.plot(xYas,regression.predict(xYas),color = "blue")
#plt.show()
print(regression.predict(regressionPoly.fit_transform([[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5]])))
#print("Makine Öğrenmesi Tahmine Hoş Geldiniz")
#bolge = input("Bölgeyi yazınız : ")
#egitim = input("Eğitimi yazınız : ")
#yas = input("Yaş Aralığı Yazınız : ")
#tahmin = abs(regression.predict(regressionPoly.fit_transform([[bolgeCevirici(bolge),egitimCevirici(egitim),yasCevirici(yas)]])))
#if tahmin <= 1.5:
#    print("Tahmin AKP")
#    print(tahmin)
#elif 1.5 < tahmin <= 2.5:
#    print("Tahmin CHP")
#    print(tahmin)
#elif 2.5 < tahmin <= 3.5:
#    print("Tahmin DİĞER")
#    print(tahmin)
#elif 3.5 < tahmin <= 4.5:
#    print("Tahmin HDP")
#    print(tahmin)
#elif 4.5 < tahmin <= 5.5:
#    print("Tahmin IYI PARTI")
#    print(tahmin)
#elif 5.5 < tahmin:
#    print("Tahmin MHP")
#    print(tahmin)

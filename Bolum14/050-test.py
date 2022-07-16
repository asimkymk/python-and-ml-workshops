import pandas as pd

notlar = pd.read_csv("grades.csv")
#column larını düzenliyoruz isteğimize göre
notlar.columns = ["Soyisim","İsim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
notlar.pop("SSN")
def hesaplayıcı(test1,test2,test3,test4,final,isim = "None", soyisim = "None"):
    ortalama = ((((test1 +test2)/2) * 20) + (((test3 + test4) / 2) * 30) + (final * 50)) / 100
    print("""Kişi ve Ortalama Bilgileri
          {} {} Puanı : {}
*******************************""".format(isim,soyisim,ortalama))
print(notlar.loc[1,:"Final"]["Test3"])    


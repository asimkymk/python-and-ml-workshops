# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:20:27 2019

@author: Asım
"""

import sqlite3 as sq
import time as tm

class Dizi():
    def __init__(self,):
        self.Dizi_baglan()
    
    def Dizi_baglan(self,):
        self.baglanti = sq.connect("dizilerVeriTabani.db")
        self.imlec = self.baglanti.cursor()
        sorgu = "Create table if not exists diziler (id INT, isim TEXT, resimUri TEXT, konu TEXT, imdb INT, yapimyili INT, tur TEXT, sezonbolum TEXT,diziUri TEXT)"
        self.imlec.execute(sorgu)
        self.baglanti.commit()
        
    def Dizi_kapat(self,):
        self.baglanti.close()
        
    def Dizi_ekle(self,diziid,isim,resimUri,konu,imdb,yapimyili,tur,sezonbolum,diziUri):
        sorgu = "Insert into diziler Values (?,?,?,?,?,?,?,?,?)"
        self.imlec.execute(sorgu,(diziid,isim,resimUri,konu,imdb,yapimyili,tur,sezonbolum,diziUri))
        self.baglanti.commit()
        
    def Dizi_sorgu(self,diziid):
        sorgu = "Select * from diziler where id = ?"
        self.imlec.execute(sorgu,(diziid,))
        liste = self.imlec.fetchall()
        if len(liste) == 0:
            return False
        else:
            return True
    
    def Dizi_guncelle(self,diziid):
        if self.Dizi_sorgu(diziid):
            isim = input("İsim : ")
            resimUri = input("Resim Uri : ")
            konu = input("Konu : ")
            imdb = input("imdb Puanı : ")
            yapimyili = int(input("Yapım Yılı : "))
            tur = input("Tür : ")
            sezonbolum = input("Sezon / Bölüm : ")
            diziUri = input("Dizi Uri : ")
            sorgu = "Update diziler set isim = ?, resimUri = ?, konu = ?, imdb = ?, yapimyili = ?, tur = ?, sezonbolum = ?, diziUri = ? where id = ?"
            self.imlec.execute(sorgu,(isim,resimUri,konu,imdb,yapimyili,tur,sezonbolum,diziUri,diziid))
            self.baglanti.commit()
    
    def Dizi_sil(self,diziid):
        if self.Dizi_sorgu(diziid):
            sorgu = "Delete from diziler where id = ?"
            self.imlec.execute(sorgu,(diziid,))
            self.baglanti.commit()
        else:
            return False
        
    def Dizi_listele(self,):
        self.imlec.execute("Select * from diziler")
        liste = self.imlec.fetchall()
        if len(liste) == 0:
            print("Hata : Serverda herhangi bir dizi bulunmuyor.")
        else:
            for dizi in liste:
                print("""
                     Dizi Bilgileri
Dizi Id                   : {}
Dizi İsim                 : {}
Dizi Resim Uri            : {}
Dizi Konu                 : {}
Dizi Imdb Puanı           : {}
Dizi Yapım Yılı           : {}
Dizi Tür                  : {}
Dizi Sezon / Bölüm Sayısı : {}
Dizi Uri                  : {}
""".format(dizi[0],dizi[1],dizi[2],dizi[3],dizi[4],dizi[5],dizi[6],dizi[7],dizi[8]))
                print("*"*25)
        tm.sleep(0.5)
                
            
    def Dizi_id_uri(self,):
        self.imlec.execute("Select id, diziUri from diziler")
        liste = self.imlec.fetchall()
        if len(liste) == 0:
            print("Hata : Serverda herhangi bir dizi bulunmuyor.")
        else:
            return liste
class SeasonEpisode():
    def __init__(self,):
        self.Sezon_baglan()
    
    def Sezon_baglan(self,):
        self.baglanti = sq.connect("dizilerVeriTabani.db")
        self.imlec = self.baglanti.cursor()
        sorgu = "Create table if not exists sezonbolum (id INT, sezon INT, bolum INT)"
        self.imlec.execute(sorgu)
        self.baglanti.commit()
        
    def Sezon_kapat(self,):
        self.baglanti.close()
    
    def Sezon_ekle(self,diziid,sezon,bolum):
        sorgu = "Insert into sezonbolum Values (?,?,?)"
        self.imlec.execute(sorgu,(diziid,sezon,bolum))
        self.baglanti.commit()
    
    def Sezon_sorgu(self,diziid):
        sorgu = "Select * from sezonbolum where id = ?"
        self.imlec.execute(sorgu,(diziid,))
        liste = self.imlec.fetchall()
        if len(liste) == 0:
            return False
        else:
            return True
        
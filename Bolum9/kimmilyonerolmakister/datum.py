# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:19:59 2019

@author: Asım
"""

import sqlite3 as sq
import time as tm
import random as rd


class basamak():
    def __init__(self,):
        self.basamakPoint()
        

class SoruHavuzu():
    def soruGoster(self,id,soru,dogruCevap,cevap1,cevap2,cevap3):
        print("")
    
    def __init__(self,):
        self.connectionStart500()
    
    def connectionStart500(self,):
        self.connection = sq.connect("havuz.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("Create table if not exists sorular500 (soruId INT, soru TEXT, dogruCevap TEXT, cevap1 TEXT, cevap2 TEXT, cevap3 TEXT)")
        self.connection.commit()
    
    def soruEkle500(self,soru,dogruCevap,cevap1,cevap2,cevap3):
        self.cursor.execute("Select * from sorular500")
        liste = self.cursor.fetchall()
        soruId = len(liste)+1
        query = "Insert into sorular500 Values (?,?,?,?,?,?)"
        self.cursor.execute(query,(soruId,soru,dogruCevap,cevap1,cevap2,cevap3))
        self.connection.commit()
        tm.sleep(2)
        print("Soru başarıyla eklendi.")
        
        print("*"*50)
        
    def soruGoster500(self,):
        self.cursor.execute("select * from sorular500")
        liste = self.cursor.fetchall()
        a = len(liste)
        soruId = rd.randint(1,a)
        query = "Select * from sorular500 where soruId = ?"
        self.cursor.execute(query,(soruId,))
        liste2 = self.cursor.fetchall()
        mixliste = rd.sample(range(2, 6), 4)
        cevap0 = mixliste[0]
        cevap1 = mixliste[1]
        cevap2 = mixliste[2]
        cevap3 = mixliste[3]
        dogrucevap =  liste2[0][2]
        print(dogrucevap)
        
        print("""

{}
        
        A -) {}
        
        B -) {}
    
        C -) {}
    
        D -) {}""".format(liste2[0][1],liste2[0][cevap0],liste2[0][cevap1],liste2[0][cevap2],liste2[0][cevap3]))
       
        cevapT = "Onay"
        
        while True:
            
        
            cevap = input("Cevap : ")
            
            
            tm.sleep(2) 
            if cevap.lower() == "a":
                cevapT = liste2[0][cevap0]
                if cevapT == dogrucevap:
                    return True
                else:
                    return False
            elif cevap.lower() == "b":
                cevapT = liste2[0][cevap1]
                if cevapT == dogrucevap:
                    return True
                else:
                    return False
            elif cevap.lower() == "c":
                cevapT = liste2[0][cevap2]
                if cevapT == dogrucevap:
                    return True
                else:
                    return False
            elif cevap.lower() == "d":
                cevapT = liste2[0][cevap3]
                if cevapT == dogrucevap:
                    return True
                else:
                    return False
            else:
                print("Lütfen bir işlem gerçekleştiriniz.")
a = SoruHavuzu()
if a.soruGoster500():
    print("Tebrikler! Sonraki soruya geçiliyor.")
else:
    print("Aaaa! Yanlış Cevap!")

        
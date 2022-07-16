# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:36:41 2019

@author: Asım
"""

import sqlite3 as sq
import time as tm



class productSettings():
    def __init__(self,):
        self.createConnection()
    
    def createConnection(self,):
        self.connection = sq.connect("veri.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("create table if not exists products (productId INT, productName TEXT,rate0 INT, rate1 INT, rate2 INT, rate3 INT, rate4 INT, rate5 INT,rateOver INT, brandId INT)")
        self.connection.commit()
        
    def connectionClose(self,):
        self.connection.close()
        print("Ürünler serverından çıkış yapıldı.")
    
    def Query(self,name,productName):
        query = "Select * from brands where brandName = ?"
        self.cursor.execute(query,(name,))
        liste = self.cursor.fetchall()
        query1 = "Select * from products where productName = ?"
        self.cursor.execute(query1,(productName,))
        liste2 = self.cursor.fetchall()
        if len(liste) == 1 and len(liste2) == 0:
            return True
        else:
            return False
    def productInfo(self,brandName,productsId,productsName,rateOver):
        print("""Ürün Bilgileri:
            - Ürün İsmi       : {}
            - Ürün Marka İsmi : {}
            - Ürün Puanı      : {}
            - Ürün Id         : {}
              """.format(productsName,brandName,rateOver,productsId))
        print("*"*50)
    def productAdd(self,productName,rate0,rate1,rate2,rate3,rate4,rate5,brandName):
        if self.Query(brandName,productName):
            self.cursor.execute("Select * from products")
            liste = self.cursor.fetchall()
            productsId = len(liste) + 1
            qux = "Select * from brands where brandName = ?"
            self.cursor.execute(qux,(brandName,))
            liste = self.cursor.fetchall()
            rateOver = ((rate0 * 0) + (rate1 * 1) + (rate2*2) + (rate3*3) + (rate4*4) + (rate5 * 5)) / (rate0+rate1+rate2+rate3+rate4+rate5)
            rateOver = round(rateOver,2)
            v = rate0 + rate1+rate2+rate3+rate4+rate5
            R = rateOver
            m = 230
            C = 3.0
            msg = ((v / (v+m)) * R) + ((m / (v+m)) * C)
            msg = round(msg,2)
            query = "Insert into products Values (?,?,?,?,?,?,?,?,?,?)"
            self.cursor.execute(query,(productsId,productName,rate0,rate1,rate2,rate3,rate4,rate5,msg,liste[0][0]))
            self.connection.commit()
            
            print("Başarıyla eklendi.")
           
            tm.sleep(2)
            self.productInfo(brandName,productsId,productName,msg)
        else:
            print("Eklemek istediğiniz ürün zaten serverda bulunuyor veya marka serverda bulunmuyor.")
     
    def productList(self,):
        query = "Select * from products"
        self.cursor.execute(query)
        liste = self.cursor.fetchall()
        if len(liste)== 0:
            print("Herhangi bir ürün bulunamadı.")
            print("*"*50)
        else:
            for i in liste:
                self.productInfo(i[9],i[0],i[1],i[8])
                tm.sleep(1)
        
    def productQuery(self,name):
        query = "Select * from products where productName = ?"
        self.cursor.execute(query,(name,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Serverda bu ürün bulunmuyor.")
            print("*"*50)
        else:
            self.productInfo(liste[0][9],liste[0][0],liste[0][1],liste[0][8])
    def productDelete(self,name):
        query = "Select * from products where productName = ?"
        self.cursor.execute(query,(name,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Silmek istediğiniz ürün zaten serverda bulunmuyor.")
            print("*"*50)
        else:
            qux = "Delete from products where productName = ?"
            
            self.cursor.execute(qux,(name,))
            self.connection.commit()
            tm.sleep(2.5)
            print("Silme işlemi başarıyla tamamlandı.")
class brandsSettings():
    def __init__(self,):
        self.createConnection()

    def createConnection(self,):
        
        self.connection = sq.connect("veri.db")

        self.cursor = self.connection.cursor()
        self.cursor.execute("Create table if not exists brands (brandId INT, brandName TEXT)")
        self.connection.commit()


    def connectionClose(self,):
        self.connection.close()
        print("Marka serverından çıkış yapıldı")
        
    def brandInfo(self,brandName, brandId):
        print("""Marka Bilgileri :
            - Marka Adı : {}
            - Marka Id  : {}
              """.format(brandName,brandId))
        print("*"*50)

    def brandAdd(self,name):
        self.cursor.execute ("Select * from brands")
        liste = self.cursor.fetchall()
    
        self.cursor.execute("Select * from brands where brandName = ?",(name,))
        listem = []
        listem = self.cursor.fetchall()
        if len(listem) == 1:
            print("Marka zaten serverda bulunuyor.")
        else:
            
        
            query  = "Insert into brands values (?,?)"
            self.cursor.execute(query,(len(liste)+1,name))
            self.connection.commit()
            print("{} başarıyla eklendi".format(name))
            print("*"*40)
            
    def brandSearch(self,name):
        query = "Select * from brands where brandName = ?"
        self.cursor.execute(query,(name,))
        liste = self.cursor.fetchall()
        if len(liste) == 1:
            self.brandInfo(liste[0][1],liste[0][0])
        else:
            print("Aradığınız marka serverda bulunmuyor.")
            
    def brandList(self,):
        self.cursor.execute("Select * from brands")
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Serverda listelenecek marka bulunmuyor.")
        else:
            for i in liste:
                self.brandInfo(i[1],i[0])
                tm.sleep(1.5)
    def brandDelete(self,name):
        query = "Select * from brands where brandName = ?"
        self.cursor.execute(query,(name,))
        liste = self.cursor.fetchall()
        
        if len(liste) == 0:
            print("Silmek istediğiniz marka serverda bulunamadı.")
        else:
            brandId = liste[0][0]
            self.cursor.execute("Select * from products where brandId = ?",(brandId,))
            liste2 = self.cursor.fetchall()
            if len(liste2) == 0:
                
                query1 = "Delete from brands where brandName = ?"
                self.cursor.execute(query1,(name,))
                self.connection.commit()
                print("{} markası başarıyla serverdan silindi.".format(name))
                print("*"*50)
            else:
                print("Silmek istediğiniz markaya ait ürün(ler) bulundu. Devam ederseniz markayla beraber markaya ait ürünler de silinecek.")
                YesOrNo = input("Devam edilsin mi ?  (EVET : E , HAYIR : H) : ")
                if YesOrNo.lower() == "e":
                    print("Silme işlemleri başladı...")
                    quer = "Delete from products where brandId= ?"
                    self.cursor.execute(quer,(brandId,))
                    self.connection.commit()
                    print("{} markasına ait ürünler başarıyla serverdan silindi.".format(name))
                    print("*"*50)
                    tm.sleep(2)
                    query1 = "Delete from brands where brandName = ?"
                    self.cursor.execute(query1,(name,))
                    self.connection.commit()
                    print("{} markası başarıyla serverdan silindi.".format(name))
                    print("*"*50)
                elif YesOrNo.lower() == "h":
                    print("İşlem iptal edildi.")
                    tm.sleep(2)

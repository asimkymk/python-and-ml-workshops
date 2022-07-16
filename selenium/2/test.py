# -*- coding: utf-8 -*-
import urllib
from selenium import webdriver
import time
import os

uri = "http://watchill.org/series"

browser = webdriver.Firefox()


diziisimleri = []
browser.get(uri)
time.sleep(1)
pageCount =1
os.mkdir("Diziler")








listem = []
sezon =  browser.find_elements_by_css_selector("span.dot")
counte = len(sezon)

time.sleep(3)
with open("episode.vbpy","w+",encoding = "UTF-8") as file:
    for kay in range(1,counte+1):
        bolumSay = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[1]/div/a["+ str(kay)+ "]/span[3]")
        bolumSayisi = bolumSay.text.replace(" Bölüm", "")
        bolumSayisi = int(bolumSayisi)
        time.sleep(1)
        
        tikla = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[1]/div/a["+str(kay) +"]")
        tikla.click()
        time.sleep(1)
       
            
        for bolum in range(1,bolumSayisi+1):
            bolumad = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[3]/div/div["+ str(kay) + "]/div/a[" +str(bolum) + "]/ul/li[3]/span")
            file.write(bolumad.text + "\n")
            

def Dondurucu(x):
    listex = []
    liste = x.split('"')
    for i in liste:
        if  "://docs.google.com/file/d" in i:
            listex.append(i)
    if len(listex) == 0:
        return False
    else:
        return listex[0]

with open("watclinks.vbpy","w+",encoding = "UTF-8") as file1:
    for kay in range(1,counte+1):
        bolumSay = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[1]/div/a["+ str(kay)+ "]/span[3]")
        bolumSayisi = bolumSay.text.replace(" Bölüm", "")
        bolumSayisi = int(bolumSayisi)
        time.sleep(1)
        
        tikla = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[1]/div/a["+str(kay) +"]")
        tikla.click()
        time.sleep(1)
       
        for bolum in range(1,bolumSayisi+1):
            
            bolumlink = browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/div/div[1]/div[3]/div/div[" + str(kay) + "]/div/a[" +str(bolum) +"]")
            bolumlinx = bolumlink.get_attribute("href")
            time.sleep(0.4)
            browser.get(bolumlinx)
            time.sleep(0.5)
            kaynakKod = browser.page_source
            if Dondurucu(kaynakKod) == False:     
                kaynaklink = browser.find_element_by_id("watchill-video-player_html5")
                src = kaynaklink.get_attribute("src")
                file1.write(src+"\n")
                time.sleep(1)
                browser.back()
            else:
                file1.write(Dondurucu(kaynakKod) + "\n")
                time.sleep(1)
                browser.back()
    
    time.sleep(1)
time.sleep(3)
browser.close()

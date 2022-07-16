# -*- coding: utf-8 -*-
import wget
from selenium import webdriver
import time
import urllib.request
import os
extension_dir = 'C:\\Users\\Asım\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\2gtwm36w.default-release\\extensions\\'
extensions = [
    '{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d}.xpi'
    ]

uri = "http://watchill.org/series?min=&max=&imdb=9"
def Yasak(x):
    yasakHarfler = [':','"','?','*','/','<','>']
    for yasak in yasakHarfler:
        if yasak in x:
            x = x.replace(yasak,"")       
    return x
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

browser = webdriver.Firefox()
for extension in extensions:
    browser.install_addon(extension_dir + extension, temporary=True)
browser.get(uri)
time.sleep(3)
for i in range(1,11):
    element = "/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/div/h5"
    text = browser.find_element_by_xpath(element)
    time.sleep(1)
    print(text.text)
    os.mkdir("Diziler\{}".format(Yasak(text.text)))
    print("*"*25)
    img = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[1]/img")
    src = img.get_attribute("src")
    dizin = "Diziler/{}".format(Yasak(text.text))
    poster = "Diziler/{}/poster.png".format(Yasak(text.text))
    with open(dizin + "/imglnk.vbpy","w+",encoding="UTF-8") as img:
        img.write(src)
    time.sleep(0.5)
    with open(dizin +"/vbPSub.vbpy","w+",encoding = "UTF-8") as konux:
        konu = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div["+str(i)+"]/div[2]/p[2]")
        konux.write(konu.text)
    time.sleep(1)
    button = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div["+str(i) + "]/a")
    anaLink = button.get_attribute("href")
    browser.get(anaLink)
    time.sleep(1.2)
    hata = browser.find_element_by_class_name("main-content")
    if hata.text == "beklenmedik hata."
        
    listem = []
    sezon =  browser.find_elements_by_css_selector("span.dot")
    counte = len(sezon)

    time.sleep(3)
    with open(dizin +"/episode.vbpy","w+",encoding = "UTF-8") as file:
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
                


    with open(dizin +"/watclinks.vbpy","w+",encoding = "UTF-8") as file1:
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


    browser.back()
    time.sleep(1)
    print("-"*30)
    time.sleep(1)
    


browser.close()
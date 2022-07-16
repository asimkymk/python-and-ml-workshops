# -*- coding: utf-8 -*-

import diziServer as ds
from selenium import webdriver

dizi = ds.Dizi()
sezonbolum = ds.SeasonEpisode()

browser = webdriver.Firefox()

tumDiziler = dizi.Dizi_id_uri()

for bilgiler in tumDiziler:
    diziid = bilgiler[0]
    uri = bilgiler[1]
    browser.get(uri)
    ds.tm.sleep(1)
    bolumListe = []
    sezon =  browser.find_elements_by_css_selector("span.dot")
    sezonSayisi = len(sezon)
    for sez in range(1,sezonSayisi+1):
        bolumSay = browser.find_element_by_xpath("/html/body/div[2]/div[5]/div/div/div[1]/div[1]/div/a["+ str(sez)+ "]/span[3]")
        bolumSayisi = bolumSay.text.replace(" Bölüm", "")
        bolumSayisi = int(bolumSayisi)
        sezonbolum.Sezon_ekle(diziid,sez,bolumSayisi)
        


dizi.Dizi_kapat()
sezonbolum.Sezon_kapat()
browser.close()
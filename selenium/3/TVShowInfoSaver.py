from selenium import webdriver
import time
import diziServer as ds

browser = webdriver.Firefox()


uri = 'http://watchill.org/series'


time.sleep(1)

browser.get(uri)

print("Site açıldı.")

time.sleep(1)

dizi = ds.Dizi()
diziid = 1

for sayfa in range(1,6):
    for i in range(1,11):
        diziAdi = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/div/h5")
        resimUri = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[1]/img")
        diziKonusu = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/p[2]")
        imdbPuan = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/div/span/b")
        yapımYil = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/ul/li[1]")
        tur = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/ul/li[2]")
        sezonBolum = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/div[2]/ul/li[3]")
        sezonbolumm = sezonBolum.text.strip("Sezon / Bölüm\n") + "ölüm"
        diziUri = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div[" + str(i) + "]/a")
        while True:
            if dizi.Dizi_sorgu(diziid):
                diziid += 1
            else:
                dizi.Dizi_ekle(diziid,diziAdi.text,resimUri.get_attribute("src"),diziKonusu.text,imdbPuan.text,yapımYil.text.strip("Yapım Yılı\n"),tur.text.strip("Tür\n"),sezonbolumm,diziUri.get_attribute("href"))
                diziid += 1
                break
    
    sonrakiSayfa = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[13]/a")
    sonrakiSayfa.click()

dizi.Dizi_listele()
dizi.Dizi_kapat()           
browser.close()

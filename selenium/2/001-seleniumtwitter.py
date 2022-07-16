# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")
time.sleep(3)

girisYap = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
girisYap.click()

time.sleep(1)
username = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
username.send_keys("asimkymk")
password.send_keys("kanarya10")
time.sleep(2)
giris = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
giris.click()
time.sleep(2)
aramaText = browser.find_element_by_xpath("//*[@id='search-query']")
aramaText.send_keys("#ekşisözlük")
time.sleep(2)
aramaButon = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[3]/div/form/span/button")
aramaButon.click()
time.sleep(2)

browser.close()
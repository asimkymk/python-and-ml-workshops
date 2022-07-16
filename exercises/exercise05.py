# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:20:04 2019

@author: Asım

Exercise: 

In this exercise, we will finish building Hangman. In the game of Hangman, 
the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) 
before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, 
we wrote the logic for guessing the letter and displaying that information to 
the user. In this exercise, we have to put it all together and add logic for 
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. 
Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses 
they have left.
Keep track of the letters the user guessed. If the user guesses a letter they 
already guessed, don’t penalize them - let them guess again.
"""
import random as rd
def Oyun(kalanhak,gelenKelime="True"):
    if gelenKelime == "True":
        print("Kalan Hakkınız : {}".format(kalanhak))
        print(" _"*kelimeharfsayısı)
prediction = 6
kelimeler = []
with open("kelimekutusu.txt","r+") as file:
    for i in file:
        kelime = i[:-1]
        kelimeler.append(kelime)
kelimesayısı = len(kelimeler)
kelimesayı = rd.randint(0,kelimesayısı-1)
kelime = kelimeler[kelimesayı]
kelimeHarfListe = []
for a in kelime:
    kelimeHarfListe.append(a)
kelimeharfsayısı = len(kelimeHarfListe)
print("ADAM ASMACA'YA HOŞ GELDİNİZ!")
Oyun(5)









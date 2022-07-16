# -*- coding: utf-8 -*-


a = "Merhaba ismim asım Bugün hava çok güzel ben bayburtta doğmuşum fenerbahçe takımını tutuyorum."
a = a.lower()
liste = []

liste = a.split()

liste.sort()

for i in liste:
    print(i)
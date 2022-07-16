# -*- coding: utf-8 -*-

import pandas as pd

orders = pd.read_table("orders.tsv")

print(orders.head())
print(orders.columns)
print(orders.shape)

print(orders.item_name.str.upper()) #stringe çevirip hepsini büyük yaptık
orders.item_name = orders.item_name.str.upper()
print(orders.item_name.str.contains("Chicken")) # hepsi false çünkü büyük harde dönüştürdük isimleri
print(orders.item_name.str.contains("CHICKEN"))
orders.choice_description = orders.choice_description.str.replace("[","") # [ yerine boşluk atadık]
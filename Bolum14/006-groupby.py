# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb-1000.csv")
print(films.head())
print(films.columns)
print(films.star_rating.mean()) #ortalama hepsinin
print(films.groupby("genre").star_rating.mean()) #türlerine göre sıralayıp ortalama alddık
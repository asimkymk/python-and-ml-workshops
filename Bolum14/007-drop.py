# -*- coding: utf-8 -*-
import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)

films = films.drop("content_rating",axis=1) # ccolumnu almadık.
films = films.drop("actors_list",axis=1) #column sildik
print(films.columns)

films = films.drop(2,axis=0) # 2. satır silindi
print(films)


# -*- coding: utf-8 -*-

import pandas as pd

youtube = pd.read_csv("USvideos.csv")
print(youtube)

print(youtube.head())

youtube.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis = 1,inplace = True)
print(youtube)
print(len(youtube.columns))

print(len(youtube.index))

print(youtube["likes"].mean())

print(youtube["dislikes"].mean())

print(youtube[youtube["views"] == youtube["views"].max()]["title"].iloc[0])

print(youtube[youtube["views"] == youtube["views"].min()]["title"].iloc[0])

print(youtube.groupby("category_id").mean()["comment_count"])

print(youtube["category_id"].value_counts())

def uzunluk(x):
    return len(x)

youtube["len_title"] = youtube["title"].apply(uzunluk)


def ayir(x):
    liste = []
    liste = x.split("|")
    return len(liste)


youtube["tags_count"] = youtube["tags"].apply(ayir)
print(youtube)

def oran(x):
    y = youtube[youtube["likes"] == x]["dislikes"].iloc[0]
    k = x + y
    if x > 0 and y == 0:
        return 1
    elif k == 0:
        return 0
    else:
        return x / k
    
youtube["rate"] = youtube["likes"].apply(oran)
youtube.sort_values("rate",ascending = False,inplace= True)
print(youtube)










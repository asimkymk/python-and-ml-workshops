

def kareleri_al():
    sonuc = []
    
    for i in range(1,6):
        sonuc.append(i**2)
    
    return sonuc

print(kareleri_al())


def generation_kareleri_al():
    for i in range(1,6):
        yield i ** 2
    

generation = generation_kareleri_al()

print(generation)
iterator = iter(generation)

print(next(iterator))
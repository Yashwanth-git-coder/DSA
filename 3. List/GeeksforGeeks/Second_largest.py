def Second_lar(l):
    if len(l) <= 1:
        return None
    
    lar = max(l)

    slar = None

    for x in l:
        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(slar, x)
    return slar


l = [10, 5, 8, 20]
sec_lar = Second_lar(l)
print(sec_lar)
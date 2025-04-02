def even_odd(l):
    even = []
    odd = []
    for x in l:
        if x % 2 == 0:
            even.append(x)
        else: 
            odd.append(x)
    return even, odd


l = [10, 41, 30, 15, 80]
even, odd = even_odd(l)
print(even)
print(odd)



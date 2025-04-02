def remove_dup(l):
    res = []
    for val in l:
        if val not in res:
            res.append(val)
            res.sort()
    return res

l = [1, 2, 2, 5, 6, 3, 3, 4, 2, 1]
print(remove_dup(l))
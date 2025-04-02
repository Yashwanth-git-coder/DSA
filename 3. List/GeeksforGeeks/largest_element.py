def largest(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
        return res
    
l = [12, 10, 22, 25, 365]
print(largest(l))
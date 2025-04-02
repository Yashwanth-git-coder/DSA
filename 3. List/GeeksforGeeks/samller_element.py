def smaler(l, x):
    s = []
    for i in l:
        if i < x:
            s.append(i)
    return s

l = [8, 100, 20, 40, 3, 7]
x = int(input("Enter X: "))
smaller = smaler(l, x)
print(f"Smaller Number then {x} are: {smaller}")
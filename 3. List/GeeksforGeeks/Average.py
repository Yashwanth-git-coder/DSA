def avgs(l):
    sum = 0
    for x in l:
        sum = sum + x
    n = len(l)
    return sum/n

l = [10, 20, 30, 40]
print(avgs(l))

# avg = int(sum(l) / len(l))
# print(avg)


def stock(l):
    profit = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            profit += l[i] - l[i-1]
    return profit


l = [1, 5, 3, 8, 12]
print(f"Profit is: {stock(l)}")

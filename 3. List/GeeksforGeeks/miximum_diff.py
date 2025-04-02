def max_difference(l):
    min_element = l[0]
    max_diff = 0

    for i in range(1, len(l)):
        max_diff = max(max_diff, l[i] - min_element)
        min_element = min(min_element, l[i])

    return max_diff

l = [2, 3, 10, 6, 4, 8, 1]
print(max_difference(l))



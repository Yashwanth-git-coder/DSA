def max_subarr(arr):
    res = arr[0]
    max_end = arr[0]

    for i in range(1, len(arr)):
        max_end = max(max_end + arr[i], arr[i])
        res = max(max_end, res)

    return res


arr = [-5, 1, -2, 3, -1, 2, -2]
print(max_subarr(arr))
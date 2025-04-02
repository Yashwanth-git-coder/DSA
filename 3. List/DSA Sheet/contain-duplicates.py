def duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return "yes"
    return "no"



arr = [1,2,3,4,5]
print(f"{duplicates(arr)}")
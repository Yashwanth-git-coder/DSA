def sorted_check(l):
    temp = l.sort()
    if l == temp:
        return True
    return False


l = [10, 5]
if sorted_check(l):
    print("Yes!")
else:
    print("No!")
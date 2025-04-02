n = int(input("Enter n: "))
count = 0
while n > 0:
    n = n//10
    count += 1
print("Number of Digits in a given number is: ", count)
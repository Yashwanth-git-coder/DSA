n = int(input("Enter the Number: "))
fact = 1
for i in range(2, n+1):
    fact = fact*i
print("Factorial of ", n, " is: ", fact)
def ispalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        dig = n%10
        rev = rev*10+dig
        n = n//10
    if temp == rev:
        return "Number is Palindrome"
    else:
        return "Number is not Palindrome"


n = int(input("Enter the Number: "))
print(ispalindrome(n))


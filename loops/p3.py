#palindrome check TC- O(log(N))  SC- O(1)

n = int(input("Enter a number: "))
num = n
result = 0
while num > 0:
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10
if n == result:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")

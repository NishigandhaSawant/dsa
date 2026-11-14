#extraction of digits
num = int(input("Enter a number: "))
while num > 0:
    lastdigit = num % 10
    print(lastdigit)
    num = num // 10

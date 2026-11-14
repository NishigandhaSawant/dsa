#armstrong number check TC- O(log(N))  SC- O(1)
n = int(input("Enter a number: "))
num_of_digits = len(str(n))
num = n
total = 0
while num > 0:
    last_digit = num % 10
    total += last_digit ** num_of_digits
    num = num // 10
if n == total:
    print(n, "is an Armstrong number")  
else:
    print(n, "is not an Armstrong number")

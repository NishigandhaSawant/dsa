# count the number of digits in a number  
# TC=O(log(N)) 
'''num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1  
   

print(count)'''

#logartihmic approach
from math import *
num = int(input("Enter a number: "))
def count_digits(n):
    if n == 0:
        return 1
    else:
        return floor(log10(n)) + 1
print(count_digits(num))

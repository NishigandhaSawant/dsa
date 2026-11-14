#print factors/ divisors of a number TC- O(N)  SC- O(1)
#brute force approach
n = int(input("Enter a number: "))
result= []

for i in range(1, num//2)+1:
    if num % i == 0:
        result.append(i)   
    else:
        continue        
        
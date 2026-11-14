# TC - O(n+m)
# SC - O(n) 

n = [2,3,4,3,3,10,3,6,3,8,6,4,9,4,2]
m = [10,11,2,9,5,67,2]

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])


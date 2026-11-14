nums = [ 2,3,4,1,2,2,3,3,5,5,11,3,4,1,1,2,2,6,7,7,7,4,2,5,6,3]

hash_map = {}
n = len(nums)

for i in range(n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)
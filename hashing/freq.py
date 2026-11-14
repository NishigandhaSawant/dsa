#freq_map/dictionary
#TC- for loop O(N) SC- O(N)
nums = [ 2,3,4,1,2,2,3,3,5,5,11,3,4,1,1,2,2,6,7,7,7,4,2,5,6,3]
freq_map = {}
for i in range(len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

print("Frequency of 2 is:", freq_map[2])
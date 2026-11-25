#minimum index
# tc O(n^2) sc O(1)
nums = [ 5, 2, 9, 1, 5, 6 ]

def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

selection_sort(nums)
print(nums)
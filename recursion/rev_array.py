#reversing an array using recursion
# array.reverse()
# array(::-1)
# two pointers
nums = [1,2,3,4,5,6,7,8,9]
def func(nums,left,right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)
def reverse_array(nums,l,r):
   self.func(nums,l,r)
   return nums

func(nums, 0, 8)
print(nums)

# TC - O(n) SC - O(n) stack space
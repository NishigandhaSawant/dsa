class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
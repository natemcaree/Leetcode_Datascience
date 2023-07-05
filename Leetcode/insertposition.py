class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
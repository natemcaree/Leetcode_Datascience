class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diffs = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], i]
            else:
                diffs[num] = i
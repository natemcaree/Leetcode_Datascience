class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        num_length = len(nums)
        for i in range(1, num_length):
            nums[i] += nums[i-1]
        return nums
    nums = [1,2,3,4]
    print(runningSum(runningSum, nums))
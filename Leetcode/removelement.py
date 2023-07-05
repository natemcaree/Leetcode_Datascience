class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        del nums[j:]
        return nums
    
    nums = [3,2,2,3]
    val = 3
    print (removeElement(removeElement, nums, val))
    
    # This is interesting
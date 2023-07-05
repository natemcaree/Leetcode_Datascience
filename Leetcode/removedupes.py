class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
                if nums[i] == nums[i+1]:
                    nums.pop(i)
                else:
                    i += 1
                
        return int(len(nums))
                
    nums = [1,2,2,3,5]
    print (removeDuplicates(removeDuplicates, nums))
    
    
    # I solved a different problem. I was saving these to a list to be read out,
    # all that needed to be returned was the number of unique numbers.
    # ex: x = [1,1,2] should return 2 
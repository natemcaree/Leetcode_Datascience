# class Solution:
#     def reverseString(self, string):
#         return string[::-1]
    
#     string = "nwj"
#     print(reverseString(reverseString, string))

# Time to complete: 30 seconds. 
# Answer: Correct

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Solution:
#     def fizzBuzz(self, int):
#         if int % 3 == 0:
#             return "Fizz"
#         elif int % 5 == 0:
#             return "Buzz"
#         elif int % 5 == 0 and int % 3 == 0:
#             return "FizzBuzz"
#         else: return str(int)
#     int = 30
#     print(fizzBuzz(fizzBuzz, int))

# Time to complete: 5 mins
# Answer: Working, syntax flaws

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Solution:
#     def factorial(self, num):
#         # Initialize result so we can iterate through loop on num 
#         result = 1
#         # Set range to start at 2 since 1 is always going to be 1
#         # i actually acts as the current number position, so we multiply it with result
#         for i in range(2, num + 1):
            
#             result *= i
#         return result
#     num = 10
#     print(factorial(factorial, num))
    
# Time to complete: 10-15 mins
# Answer: Not working, idea was close. Check notes above.

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         num_indices = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_indices:
#                 return [num_indices[complement], i]
#             num_indices[num] = i
#         return []  ## Return an empty list if no solution is found

            
            
#     num = [1,2,5]
#     target = 7
#     print(twoSum(twoSum, num, target))
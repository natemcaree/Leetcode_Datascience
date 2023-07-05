class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        step2 = 2
        step3 = 3

        for _ in range(4, n+1):
            current_step = step2 + step3
            step2 = step3
            step3 = current_step

        return step3
        
        
#You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

# Solution: take last 2 solutions and combine

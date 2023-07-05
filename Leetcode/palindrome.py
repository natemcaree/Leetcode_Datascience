class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: 
            return False
        
        answer = int(str(x)[::-1])
        if answer == x: return True
        else: return False
    x = -10
    isPalindrome(isPalindrome, x)
            
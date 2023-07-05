class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        split_haystack = list(haystack)
        print(split_haystack)
        split_needle = list(needle)
        print(split_needle)
        
        
        for i, char in enumerate(split_haystack):
            if split_haystack[i:i+len(split_needle)] == split_needle:
                return i
        
        return -1
        
        
    haystack = "onetwoone"
    needle = "two"    
    print(strStr(strStr, haystack, needle))
        
        # Method: 
            # split string into alphas 
            # match string of needle alpha to haystack alpha
            # if needle check is broken, restart. 
            # if end of line, needle = -1
        
        
    # MUCH EASIER SOLUTION - 
    # class Solution:
    #     def strStr(self, haystack: str, needle: str) -> int:
    #     return haystack.find(needle)
    
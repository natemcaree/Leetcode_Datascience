class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # rev_s = s[::-1].lstrip()
        # count = 0
        # print(rev_s)
        # for char in rev_s:
        #     if char != " ":
        #         count += 1
        #     else:   
        #         break
        # return count
        return len(s.strip().split()[-1])
    
    words = "womp doomp pop bloom    "
    print(lengthOfLastWord(lengthOfLastWord, words))
    
    # GOAL: Find length of last word.
    # METHOD: Start in reverse order, and check if it is a space. If it is a space, go back one more. 
    # Then, continue going back until you see another space. Take the count of the indexes you pass through and return a final output
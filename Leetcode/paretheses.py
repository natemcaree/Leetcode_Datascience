class Solution:
    def isValid(self, s: str) -> bool:
        lst = list(s)
        stack = []
        opening = "([{"
        closing = ")]}"
        pairs = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or pairs[stack.pop()] != char:
                    return False

            return len(stack) == 0   
       
       
    #    lst=[]
    #     dic={'(':')','{':'}','[':']'}
    #     left="([{"
    #     for i in s:
    #         if i in left:
    #             lst.append(dic[i])
    #         elif lst and lst[-1]==i:
    #             lst.pop()
    #         else:return False
    #     return not lst
       
       
    s = "[()]"
    print(isValid(isValid, s))
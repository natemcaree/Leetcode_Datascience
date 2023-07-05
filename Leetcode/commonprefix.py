class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ''
    
        if not strs:
            return common_prefix
        
        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return common_prefix
            
            common_prefix += char
        
        return common_prefix

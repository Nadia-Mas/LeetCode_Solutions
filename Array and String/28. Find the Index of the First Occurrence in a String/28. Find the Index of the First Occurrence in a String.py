class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        length = len(needle)
        
        for i in range(len(haystack)):
            if haystack[i:i+length]==needle:
                return i
        else:            
            return -1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         ans = ""
#         i =0
#         count = 0

#         if len(s)==1:
#             return 1
#         else:
#             while i < len(s):
#                 if s[i] not in ans:
#                     ans += s[i]                   
#                 else:
#                     ans  = ans[(ans.index(s[i])+1):]+ s[i]
#                 i +=1
#                 count = max(count, len(ans))
#             return(count)

        h = {} # hash map of most recent position of each character that has appeared
        start = longest = 0
        for i, char in enumerate(s):
            if char in h: 
                start = max(start, h[char] + 1)
            h[char] = i
            longest = max(longest, i - start + 1)
        return longest
                    
                                    



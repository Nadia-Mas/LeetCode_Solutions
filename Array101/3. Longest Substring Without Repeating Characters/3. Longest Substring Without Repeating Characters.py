class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        i =0
        count = 0

        if len(s)==1:
            return 1
        else:
            while i < len(s):
                if s[i] not in ans:
                    ans += s[i]
                    
                else:
                    ans  = ans[(ans.index(s[i])+1):]+ s[i]
                   
                i +=1
                count = max(count, len(ans))
                
            return(count)
        #Approach 02
        # seen = {}
        # l = 0
        # output = 0
        # for r in range(len(s)):
        #     """
        #     If s[r] not in seen, we can keep increasing the window size by moving right pointer
        #     """
        #     if s[r] not in seen:
        #         output = max(output,r-l+1)
        #     """
        #     There are two cases if s[r] in seen:
        #     case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
        #     case2: s[r] is not inside the current window, we can keep increase the window
        #     """
        #     else:
        #         if seen[s[r]] < l:
        #             output = max(output,r-l+1)
        #         else:
        #             l = seen[s[r]] + 1
        #     seen[s[r]] = r
        # return output
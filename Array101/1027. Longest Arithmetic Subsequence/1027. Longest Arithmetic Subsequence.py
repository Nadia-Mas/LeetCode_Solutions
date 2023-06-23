class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[{} for _ in range(n)]
        ans=0
        for i in range(n):
            dp[i][0]=1
            for j in range(i):
                diff=nums[i]-nums[j]

                if diff not in dp[j]:
                    dp[i][diff]=2

                else:
                    dp[i][diff]=dp[j][diff]+1

            ans=max(ans,max(dp[i].values()))

        return ans 
class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        #Approach 01
        # n=len(nums)
        # dp=[{} for _ in range(n)]
        # ans=0
        # for i in range(n):
        #     dp[i][0]=1
        #     for j in range(i):
        #         diff=nums[i]-nums[j]

        #         if diff not in dp[j]:
        #             dp[i][diff]=2

        #         else:
        #             dp[i][diff]=dp[j][diff]+1

        #     ans=max(ans,max(dp[i].values()))

        return ans 
        #Approach 02
        seq = []
 
        for num in nums:
            d = collections.defaultdict(int)
            for i in range(len(seq)):
                d[nums[i]-num] = seq[i][nums[i]-num] + 1
            seq.append(d)
        
        return max(max(d.values()) for d in seq) + 1
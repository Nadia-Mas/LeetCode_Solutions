class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])

        return ans
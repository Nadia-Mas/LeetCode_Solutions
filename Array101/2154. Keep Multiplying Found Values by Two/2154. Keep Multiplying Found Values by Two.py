class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:

        while original in nums:
            original = original*2
        else:
            return original
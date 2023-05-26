class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
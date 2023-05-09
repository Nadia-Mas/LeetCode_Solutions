class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_indx=i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[i]:
                    nums[min_indx], nums[j]=nums[j], nums[min_indx]
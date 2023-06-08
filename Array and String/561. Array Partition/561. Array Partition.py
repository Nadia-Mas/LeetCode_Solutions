class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        
        nums = sorted(nums)
        max_sum = 0
        i , j = 0 , 1
        
        while j <(len(nums)):
            max_sum += min(nums[i], nums[j])
            i = i +2
            j = j+ 2
            
        return max_sum
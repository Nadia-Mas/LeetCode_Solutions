class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        m = max(nums)
        i = nums.index(m)
        nums.remove(m)
        if 2*max(nums) <= m:
            return i
        return -1
        
        
        
#         index = nums.index(max(nums))
#         nums = sorted (nums)
#         max_ele = nums[-1]
#         counter =0
        
#         for i in range(len(nums)-1):
#             if (nums[i]*2 <= max_ele):
#                 counter +=1
                
#         if counter == len(nums)-1:
#             return index
#         else: return -1
        
        
        
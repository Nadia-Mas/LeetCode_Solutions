class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
#Approach 01:        
        left_sum , right_sum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            right_sum -=ele
            if left_sum == right_sum:
                return idx
            left_sum +=ele
        return -1
#Time Complexity: O(n)    
    
#Approach 02:        
#         for i in range(len(nums)):
#             left_sum = []
#             right_sum = []
#             left_sum_count = 0
#             right_sum_count = 0
            
#             for j in range(0,i):
#                 left_sum_count +=nums[j]
#             left_sum.append(left_sum_count)
            
#             for k in range(i+1, len(nums)):
#                 right_sum_count += nums[k]
#             right_sum.append(right_sum_count)
            
#             if right_sum == left_sum:
#                 return i
#             else:
#                 continue
#         return -1
# Time Complexity =O(n**2)  Tooooo expensive :(
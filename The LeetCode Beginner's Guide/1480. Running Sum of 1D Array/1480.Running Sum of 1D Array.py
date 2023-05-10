class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        
        nums2=[] 
        nums2.insert(0, nums[0])

        for i in range(1,len(nums)):
            nums2.append(nums[i]+nums2[i-1])

        nums=nums2
        return nums
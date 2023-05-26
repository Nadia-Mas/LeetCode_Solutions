class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ##Approach 01##
        # if target not in nums:
        #     return[-1, -1]
        # else:
        #     po = nums.index(target)
        #     min, max = po, po
        #     for i in range(po+1, len(nums)):
        #         if nums[i]==target:
        #             max =i
                    
        # return [min, max]

        ##Approach 02##
        if target not in nums:
            return[-1, -1]

        def search(x):
            lo, hi = 0, len(nums)
            while lo<hi:
                mid = (lo+hi)//2
                if nums[mid]<x:
                    lo = mid+1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target+1)-1

        if lo<=hi:
            return[lo, hi]
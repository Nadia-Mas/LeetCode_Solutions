class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans =[]
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[j]< nums[i]:
                    counter +=1
            ans.append(counter)
        return ans
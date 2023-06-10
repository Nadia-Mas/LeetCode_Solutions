class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Approach 01
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums
    
        #Approach 02
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
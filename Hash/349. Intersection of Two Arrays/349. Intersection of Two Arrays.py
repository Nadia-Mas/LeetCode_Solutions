class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        numset1, numset2 = set(nums1), set(nums2)
        
        return(numset1.intersection(numset2))
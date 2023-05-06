class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for j in range(len(nums2)):
            nums1.insert(m, nums2[j])
            m+1
                
                        
        x= len(nums1)
        for i in range(x-(m+n)):
            nums1.pop()
            
        nums1.sort()
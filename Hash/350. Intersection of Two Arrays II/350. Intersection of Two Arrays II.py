from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap1 = Counter(list(nums1))
        hashmap2 = Counter(list(nums2))
        
        res= (hashmap1 & hashmap2)
       
        return(res.elements())
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
        #approach 02#
        # if m < 1:
        #     nums1[:] = nums2[:n]
        # elif n < 1:
        #     nums1[:] = nums1[:m]
        # else:
        #     nums1[:] = sorted(nums1[:m] + nums2[:n])

        #approach 03#
        # i, j, k = m-1, n-1, m+n-1

        # while j >= 0:
        #     if i >= 0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #         k -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #         k -= 1
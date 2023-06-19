class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        #approach 01
        # ans=[]
        # temp = []
        # temp_2 = []

        # for n in nums1:
        #     if n not in nums2 and n not in temp:
                
        #         temp.append(n)
                
        # for m in nums2:   
        #     if m not in nums1 and m not in temp_2 :
        #         temp_2.append(m)
        # ans.append(temp)
        # ans.append(temp_2)
        # return ans

        #approach 02
        #return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]
        #Approach 03
        # define set to store elements
        # s1 = set(nums1)
        # s2 = set(nums2)

        # # define output
        # out = [[],[]]

        # # adding the elements to output if not contains in the set
        # for i in s1:
        #     if i not in s2:  
        #         out[0].append(i)
        # for i in s2:
        #     if i not in s1:
        #         out[1].append(i)
        
        # return out
    #Approach 04
            n1=set(nums1)
        n2=set(nums2)
        r1=list(set(x for x in nums1 if x not in n2))
        r2=list(set(x for x in nums2 if x not in n1))
        return [r1,r2]
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        #Approach 01
        sum_dict={0:-1}
        total=0
        for i,val in enumerate(nums):
            total+=val
            remain=total % k
            if remain not in sum_dict:
                sum_dict[remain]=i
            elif i - sum_dict[remain]>1:
                print (remain)
                return True
        return False


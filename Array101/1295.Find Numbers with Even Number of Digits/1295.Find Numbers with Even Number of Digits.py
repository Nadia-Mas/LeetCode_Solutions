class Solution:
    def findNumbers(self, nums: list[int]) -> int:

        counter = 0
        for i in range(len(nums)):
            a = str(nums[i])
            b = len(a)

            if b % 2 == 0:
                counter += 1

        return counter
    
        #return len([x for x in nums if  len(str(x))%2==0])
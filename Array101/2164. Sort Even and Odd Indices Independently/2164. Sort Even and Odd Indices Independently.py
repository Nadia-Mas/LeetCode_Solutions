class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        ans = []
        odd = []
        even = []

        #Even
        for i in range(0, len(nums), 2):
            even.append(nums[i])
        even.sort()
        
        #Odd
        for j in range(1, len(nums), 2):
            odd.append(nums[j])
        odd.sort()
        odd = odd[::-1]

        odd_idx , even_idx = 0 , 0

        for i in range(len(nums)):

            if i %2 ==0:
                ans.insert(i,even[even_idx])
                even_idx +=1
            else:
                ans.insert(i,odd[odd_idx])
                odd_idx +=1
        return ans
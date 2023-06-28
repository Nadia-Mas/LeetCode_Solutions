class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #Approach 01
        # lookup ={i:[] for i in nums}
        # for j in range(len(nums)):
        #     if nums[j] in lookup.keys():
        #         lookup[nums[j]].append(j)

        # max_num = 0
        # for k in lookup:
        #     if len(lookup[k])>max_num:
        #         max_num = len(lookup[k])
        #         max_k = k
        # return max_k
        #Approach 02
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol
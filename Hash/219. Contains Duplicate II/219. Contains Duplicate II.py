class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #Approach 01
        # lookup={}
        # for i  in range(len(nums)):
        #         number=nums[i]
        #         if number in lookup and i-lookup[number]<=k:
        #             return True
        #         else:
        #             lookup[number]=i
        #Approach 02
        last_seen_index = {}
        for idx, x in enumerate(nums):
            if x in last_seen_index and idx - last_seen_index[x] <= k:
                return True
            last_seen_index[x] = idx
        return False
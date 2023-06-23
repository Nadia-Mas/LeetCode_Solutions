import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        # for i in range(k-1):
        #     temp = max(nums)
        #     nums.pop(nums.index(temp))
        # return(max(nums))
        if not nums or not k or k < 0:
            return None
        maxheap, res = [], None
        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            res = -heapq.heappop(maxheap)
        return res
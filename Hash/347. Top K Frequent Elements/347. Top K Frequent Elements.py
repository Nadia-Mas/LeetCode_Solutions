from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        return [c[0] for c in Counter(nums).most_common(k)]
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n != 0:
            if n & 1 ==1:
                counter +=1
            n = n >> 1
        return counter
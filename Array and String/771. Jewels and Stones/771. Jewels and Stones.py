class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_l = [i for i in jewels]
        stone_l = [i for i in stones]
        counter = 0
        
        for i in stone_l:
            if i in jewel_l:
                counter +=1
            else:
                continue
        return counter
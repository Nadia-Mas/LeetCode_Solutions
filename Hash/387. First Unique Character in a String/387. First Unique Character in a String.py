from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0: return -1
        occ = Counter(list(s))
        
        for k,v in occ.items():
            if v==1: return s.index(k)
            
        return -1
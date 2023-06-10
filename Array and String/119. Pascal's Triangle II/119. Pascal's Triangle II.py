class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        r = [1]
        for i in range(1,rowIndex+1):
            r.append(int(r[-1]*(rowIndex-i+1)/i) )
        return r
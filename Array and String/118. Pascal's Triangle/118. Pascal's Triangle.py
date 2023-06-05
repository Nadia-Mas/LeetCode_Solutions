class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        res.append([1])
        intermediate = []
        
        for i in range(numRows-1):
            intermediate = [1]
            for j in range(i):
                intermediate.append(res[i][j]+res[i][j+1])
            intermediate.append(1)
            res.append(intermediate)
        return res
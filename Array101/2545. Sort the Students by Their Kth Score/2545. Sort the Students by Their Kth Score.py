class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        ##Approach 01
        target =[]
        
        for i in range(len(score)):
            target += [[score[i][k], score[i]]]
        print(score)

        def cmp(score):
            return score[0]

        target = sorted(target, key= cmp)[::-1]

        print(target)

        ans = []
        for i in range(len(target)):
            score[i] = target[i][1]

        return score
    
        ##Approach 02
        #return sorted(score, key = lambda i: -i[k])        
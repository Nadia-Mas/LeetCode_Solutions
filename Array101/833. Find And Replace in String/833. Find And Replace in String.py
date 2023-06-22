class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: List[str]) -> str:
        #Approach 01
        # lookup = {i:(src, trg) for i, src, trg in zip(indices, sources, targets)}
        # i, result = 0 , ""

        # while i <len(s):
        #     if i in lookup and s[i:].startswith(lookup[i][0]):
        #         result += lookup[i][1]
        #         i +=len(lookup[i][0])
        #     else:
        #         result +=s[i]
        #         i +=1
        # return result

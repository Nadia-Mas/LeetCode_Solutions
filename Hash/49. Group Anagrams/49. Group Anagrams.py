class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #Aproach 01   
        lookup = defaultdict(list)
        for i in strs:
            lookup[str(sorted(i))].append(i)
        return lookup.values()
    
    #Approach 02
        # result = {}
        # for s in strs:
        #     key = str(sorted(s))
        #     if key in result:
        #         result[key] += [s]
        #     else:
        #         result[key] = [s]
        # return list(result.values())
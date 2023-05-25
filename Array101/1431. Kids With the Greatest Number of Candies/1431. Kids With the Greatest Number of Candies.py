class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #Approach 01
        result=[]
        for candy in candies:
            now=candy+extraCandies

            n = True
            for candy2 in candies:
                if now<candy2:
                    n= False
            result.append(n)
        return result
    
        #Approach 02
        #  maxval = max(candies)
        # return list(x + extraCandies >= maxval  for x in candies)
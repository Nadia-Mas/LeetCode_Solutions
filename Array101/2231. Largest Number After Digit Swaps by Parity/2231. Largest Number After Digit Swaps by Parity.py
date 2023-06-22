class Solution:
    def largestInteger(self, num: int) -> int:
        #Approach 01
       # nums= str(num)
        n = len(str(num))
        digit_list = [int(i) for i in str(num)]
 
        odds=[]
        evens=[]

        for i in digit_list:
            if i%2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        
        odds.sort()
        evens.sort()

        ans = [odds.pop() if digit_list[d]%2 else evens.pop() for d in range(n)]
        return (sum([d*10**(len(ans)-i-1) for i,d in enumerate(ans)]))
        #Approach 02
        # n = len(str(num))
        # arr = [int(i) for i in str(num)]
        # odd, even = [], []
        # for i in arr:
        #     if i % 2 == 0:
        #         even.append(i)
        #     else:
        #         odd.append(i)
        # odd.sort()
        # even.sort()
        # res = 0
        # for i in range(n):
        #     if arr[i] % 2 == 0:
        #         res = res*10 + even.pop()
        #     else:
        #         res = res*10 + odd.pop()
        # return res




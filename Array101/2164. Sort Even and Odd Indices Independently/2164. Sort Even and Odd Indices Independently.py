class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        #Approach 01
        # ans = []
        # odd = []
        # even = []

        # #Even
        # for i in range(0, len(nums), 2):
        #     even.append(nums[i])
        # even.sort()
        
        # #Odd
        # for j in range(1, len(nums), 2):
        #     odd.append(nums[j])
        # odd.sort()
        # odd = odd[::-1]

        # odd_idx , even_idx = 0 , 0

        # for i in range(len(nums)):

        #     if i %2 ==0:
        #         ans.insert(i,even[even_idx])
        #         even_idx +=1
        #     else:
        #         ans.insert(i,odd[odd_idx])
        #         odd_idx +=1
        # return ans
        #Approach 02
                return reduce(add, zip_longest(sorted(nums[::2]), sorted(nums[1::2], reverse=True)))[:-1 if len(nums) % 2 else None]
        #Explain:
        # evens = sorted(nums[::2])
        # odds = sorted(nums[1::2], reverse=True)
        # #                       🠓 Made flat zip(), see stackoverflow.com/questions/61943924/python-flat-zip
        # total = [num for num in chain.from_iterable(itertools.zip_longest(evens, odds)) if num is not None]
        # #                                                                               🠑 zip_longest() inserts 'None' for two lists with different length, we must delete it

        # return total
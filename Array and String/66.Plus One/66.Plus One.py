class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
#Approach 01
        strings =""
        for number in digits:
            strings += str(number)

        temp =str(int(strings) +1)
        return[int(temp[i]) for i in range(len(temp))]
#Approach 02
        # num=int(''.join(str(e)for e in digits))+1
        # res = map(int,str(num))
        # return res
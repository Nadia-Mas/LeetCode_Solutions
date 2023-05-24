class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        strings =""
        for number in digits:
            strings += str(number)

        temp =str(int(strings) +1)
        return[int(temp[i]) for i in range(len(temp))]
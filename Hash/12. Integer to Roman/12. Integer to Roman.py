class Solution:
    def intToRoman(self, num: int) -> str:
        integer_n ={1:"I",4:"IV", 5:"V",9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D",900:"CM", 1000:"M"}
        r =""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n<=num and n != 0:
                r += integer_n[n]
                num -=n
        return r
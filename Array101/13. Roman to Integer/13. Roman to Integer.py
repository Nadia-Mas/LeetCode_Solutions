class Solution:
    def romanToInt(self, s: str) -> int:
        #Approach 01
        roman_n = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i in range(len(s)-1):
            if roman_n[s[i]]< roman_n[s[i+1]]:
                ans -= roman_n[s[i]]
            else:
                ans += roman_n[s[i]]
        return ans + roman_n[s[-1]]
        #Approach 02
        # table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # convert = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX", "XC": "LXXXX", "CD":  "CCCC", "CM": "DCCCC"}
        # s_copy = s
        # for key, value in convert.items():
        #     s_copy = s_copy.replace(key, value)
        # return sum([table[i] for i in s_copy])
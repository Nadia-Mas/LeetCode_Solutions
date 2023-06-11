class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])
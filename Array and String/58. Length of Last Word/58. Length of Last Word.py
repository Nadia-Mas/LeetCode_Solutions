class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = s.split()
        return (len(sentence[-1]))
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in {'[', "{", "("}:
                stack.append(i)
            else:
                if stack == []:
                    return False
                poping = stack.pop()
                if (poping=="(" and i!=")") or (poping =="{" and i!="}") or (poping =="[" and i !="]"):
                    return False
        return stack == []
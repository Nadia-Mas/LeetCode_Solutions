class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        x_max=0
        for acc in accounts:
            tot = sum(acc)
            if tot>x_max:
                x_max=tot
        return x_max

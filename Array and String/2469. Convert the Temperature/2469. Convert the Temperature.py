class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = [celsius+273.15,celsius*1.80+32.00]
        return ans
#Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.
#Input: num = "51230100"
#Output: "512301"

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(int(num[::-1]))[::-1]

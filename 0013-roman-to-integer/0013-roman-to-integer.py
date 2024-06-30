class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        seen = s[0]
        num = 0
        for roman in s:
            if roman_dict[seen] < roman_dict[roman]:
                num += (roman_dict[roman]-roman_dict[seen]*2)

            else:
                num += roman_dict[roman]

            seen = roman
            
        return num
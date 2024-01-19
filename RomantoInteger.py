class Solution:
    def romanToInt(self, s: str) -> int:
        roman = s
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman) - 1, -1, -1):
            if i < len(roman) - 1 and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
                result -= roman_dict[roman[i]]
            else:
                result += roman_dict[roman[i]]
        return result

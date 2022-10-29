class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        result = 0
        lenth = len(s)
        for i in range(lenth):
            if s[i] == "I" and i < lenth - 1:
                if s[i + 1] == "V":
                    result -= 1
                elif s[i + 1] == "X":
                    result -= 1
                else:
                    result += roman["I"]
            elif s[i] == "X" and i < lenth - 1:
                if s[i + 1] == "L":
                    result -= 10
                elif s[i + 1] == "C":
                    result -= 10
                else:
                    result += roman["X"]
            elif s[i] == "C" and i < lenth - 1:
                if s[i + 1] == "D":
                    result -= 100
                elif s[i + 1] == "M":
                    result -= 100
                else:
                    result += roman["C"]
            else:
                result += roman[s[i]]
        return result

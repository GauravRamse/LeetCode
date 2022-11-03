class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

        val = roman[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            current = roman[s[i]]
            next = roman[s[i + 1]]
            if (current < next):
                val = val - roman[s[i]]
            elif (current > next):
                val = val + roman[s[i]]
            elif (current == next):
                val = val + roman[s[i]]

        return val


if __name__ == "__main__":
    nums = "III"
    obj = Solution()
    result = obj.romanToInt(nums)
    print(f"Roman to numer is {result}")
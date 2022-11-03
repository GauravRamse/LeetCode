
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
############################################################################
## Solution 1
class Solution:

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
############################################################################
# Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        input_num = x
        reverse_num = 0

        while x > 0:
            reverse_num = reverse_num * 10 + x % 10
            x = x // 10

        return input_num == reverse_num
############################################################################
if __name__ == "__main__":
    nums = 121
    obj = Solution()
    result = obj.isPalindrome(nums)
    print(f"Result for palindrome number is {result}")

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import  List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pref = ""
        if len(strs[0]) > 0:

            count = 0
            flag = True
            while flag:
                try:
                    temp = strs[0][count]
                    for chr in strs:

                        if temp == chr[count]:
                            temp = chr[count]
                        else:
                            flag = False
                            temp = ""
                            break

                    count += 1
                    longest_pref += temp
                    if len(longest_pref) > 0:
                        temp = longest_pref[-1]
                except:
                    break

        return longest_pref


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    obj = Solution()
    result = obj.longestCommonPrefix(strs)
    print(f"Longest prefix is {result}")






from typing import List
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)

        for idx_i in range(len_nums):

            for idx_j in range(idx_i + 1, len_nums):

                if nums[idx_i] + nums[idx_j] == target:
                    result = [idx_i, idx_j]
                    break
        return result

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    result = obj.twoSum(nums, target)
    print(f"Output result is {result}")
from typing import List


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for num in nums:
            single ^= num
        return single


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # n ^ 0 = n
        for n in nums:
            res = n ^ res

        return res


# test
if __name__ == '__main__':
    print(Solution().singleNumber([2, 4, 5, 4, 5, 2, 6, 7, 7]))

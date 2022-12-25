from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        res = {}

        for n in nums:

            if n in res:
                return True
            res[n] = True
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))
    assert (Solution().containsDuplicate(nums) == True)

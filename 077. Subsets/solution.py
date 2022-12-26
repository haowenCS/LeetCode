from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # O(n * 2^n)
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
    # assert (Solution().twoSum(nums, target) == [0, 1])

    # tmp = nums.copy()
    #
    #
    # # print(id(nums[-1]))
    # # print(id(tmp[-1]))
    #
    # nums[-1][0] = 100
    #
    # # print(id(nums[-1]))
    # # print(id(tmp[-1]))
    # print(tmp)
    # print(nums)
    #
    # # list:copy: shallow copy, create a new object referencing to the same object. numbers are different object,
    # # if you modify the list inside the list, you can see the difference of shallow copy vs deep copy.



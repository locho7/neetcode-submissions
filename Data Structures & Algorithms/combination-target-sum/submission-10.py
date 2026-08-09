class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i: int, c: List[int], cSum: int):
            if cSum == target:
                res.append(c.copy())
                return 

            if i >= len(nums) or cSum > target:
                return


            dfs(i, c + [nums[i]], cSum + nums[i])
            dfs(i + 1, c, cSum)

        dfs(0, [], 0)
        return res
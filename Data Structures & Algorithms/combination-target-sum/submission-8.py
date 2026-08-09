class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination, cSum):
            if cSum == target:
                res.append(combination.copy())
                return

            if (i >= len(nums) or cSum > target):
                return
            
            combination.append(nums[i])
            dfs(i, combination, cSum + nums[i])

            combination.pop()
            dfs(i + 1, combination, cSum)
 
        dfs(0, [], 0)
        return res
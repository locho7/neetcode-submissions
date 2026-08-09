class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, cSum):
            if cSum == target:
                res.append(combination.copy())
                return

            if (i >= len(nums) or cSum > target):
                return
            
            combination.append(nums[i])
            dfs(i, cSum + nums[i])

            combination.pop()
            dfs(i + 1, cSum)
 
        dfs(0, 0)
        return res
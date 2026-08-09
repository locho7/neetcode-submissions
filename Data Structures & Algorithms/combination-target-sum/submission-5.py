class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        cSum = 0

        def dfs(i):
            nonlocal cSum
            if cSum == target:
                res.append(combination.copy())
                return

            if (i >= len(nums) or cSum > target):
                return
            
            combination.append(nums[i])
            cSum += nums[i]
            dfs(i)

            combination.pop()
            cSum -= nums[i]
            dfs(i + 1)
 
        dfs(0)
        return res
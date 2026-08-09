class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i: int, c: List[int], cSum: int):
            if cSum == target:
                res.append(c.copy())
                return 

            for j in range(i, len(nums)):
                if cSum + nums[j] > target:
                    return;
                    
                c.append(nums[j])
                dfs(j, c, cSum + nums[j])
                c.pop()

        dfs(0, [], 0)
        return res
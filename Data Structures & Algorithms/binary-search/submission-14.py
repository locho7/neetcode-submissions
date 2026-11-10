class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            m = (lo + hi) // 2
            print(m, lo, hi)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                hi = m
            else:
                lo = m + 1
        
        return -1

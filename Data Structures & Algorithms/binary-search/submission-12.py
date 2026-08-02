class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            med = (hi - lo) // 2 + lo
            print(med)
            if nums[med] == target:
                return med
            if nums[med] > target:
                hi = med
            if nums[med] < target:
                lo = med + 1
        return -1
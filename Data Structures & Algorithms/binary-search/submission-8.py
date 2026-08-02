class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return searchHelper(nums, target, 0, len(nums))

def searchHelper(nums: List[int], target: int, lo: int, hi: int) -> int:
    if hi - lo == 1:
        return lo if nums[lo] == target else -1
    
    med = lo + (hi - lo) // 2
    if nums[med] == target:
        return med
    elif nums[med] > target:
        return searchHelper(nums, target, lo, med)
    elif nums[med] < target:
        return searchHelper(nums, target, med, hi)

    

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stored = set()
        for num in nums:
            if num in stored:
                return True
            stored.add(num)
        return False
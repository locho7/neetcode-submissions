class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        
        while lo < hi:
            dif = target - numbers[hi]

            if dif == numbers[lo]:
                return [lo + 1, hi + 1]
            elif dif > numbers[lo]:
                lo += 1
            else:
                hi -= 1




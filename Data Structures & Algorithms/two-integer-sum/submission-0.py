class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in numsDict:
                return [numsDict[dif], i]

            if nums[i] not in numsDict:
                numsDict[nums[i]] = i

        return None
            
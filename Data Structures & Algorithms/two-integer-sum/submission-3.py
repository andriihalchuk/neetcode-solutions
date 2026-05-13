class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in prev:
                return [prev[rest], i]
            prev[nums[i]] = i
        return
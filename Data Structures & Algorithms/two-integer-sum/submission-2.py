class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in diff:
                return [diff[rest], i]
            diff[nums[i]] = i
            
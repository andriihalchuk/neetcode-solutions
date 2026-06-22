class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        max_count = 0
        for i in snums:
            if i - 1 in snums:
                continue
            count = 1
            while i + 1 in snums:
                i += 1
                count += 1
            if count > max_count:
                max_count = count

        return max_count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        counts = []
        for i in snums:
            count = 1
            if i - 1 in snums:
                continue
            while i + 1 in snums:
                i += 1
                count += 1
            counts.append(count)
        if not nums:
            return 0
        return max(counts)

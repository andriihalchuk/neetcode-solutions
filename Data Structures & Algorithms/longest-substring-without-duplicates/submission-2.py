class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in encountered:
                l = max(l, encountered[s[r]] + 1)
            encountered[s[r]] = r
            res = max(res, r - l + 1)
        return res
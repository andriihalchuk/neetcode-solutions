class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        if len1 > len(s2):
            return False

        count = [0] * 26

        for c in s1:
            count[ord(c) % 26] += 1

        for l in range(len(s2) - len1 + 1):
            chars = [0] * 26
            r = l + len1
            for c in range(l, r):
                chars[ord(s2[c]) % 26] += 1
            if chars == count:
                return True

        return False

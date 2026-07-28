class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        if len1 > len(s2):
            return False

        count = [0] * 26
        chars = [0] * 26

        for i in range(len1):
            count[ord(s1[i]) % 26] += 1
            chars[ord(s2[i]) % 26] += 1

        if chars == count:
                return True

        for l in range(len(s2) - len1):
            r = l + len1
            chars[ord(s2[r]) % 26] += 1
            chars[ord(s2[l]) % 26] -= 1
            if chars == count:
                return True
            
        return False

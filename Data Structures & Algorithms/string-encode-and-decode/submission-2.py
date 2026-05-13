class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for s in strs:
            coded += str(len(s)) + "#" + s
        return coded


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            j += 1
            ans.append(s[j : j + size])
            i = j + size
        return ans

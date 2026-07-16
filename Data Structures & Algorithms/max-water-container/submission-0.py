class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        i, j = 0, len(heights) - 1
        while i != j:
            vol = min(heights[i], heights[j]) * (j - i)
            maxVol = max(vol, maxVol)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxVol
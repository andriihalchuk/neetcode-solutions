class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxRec = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, hgt = stack.pop()
                maxRec = max(maxRec, (i - idx) * hgt)
                start = idx
            stack.append((start, h))
        
        for i, h in stack:
            maxRec = max(maxRec, (len(heights) - i) * h)

        return maxRec

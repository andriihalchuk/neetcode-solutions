class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxLeft = 0
        maxRight = 0

        for i in range(len(height)):
            maxLeft = max(maxLeft, height[i])
            maxL.append(maxLeft)
        

        for j in range(len(height) - 1, 0, -1):
            maxRight = max(maxRight, height[j])
            maxL[j] = min(maxL[j], maxRight)

        res = 0
        for k in range(len(height) - 1):
            water = maxL[k] - height[k]
            if water < 0:
                continue
            else: 
                res += water
        print(maxL)
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if the value we encounter is greater than the top of the stack then subtract indices and add to result
        # if lesser then add to the stack

        stack, res = [], [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]:
                stackVal, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
            
        return res
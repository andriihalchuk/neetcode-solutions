class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if the value we encounter is greater than the top of the stack then subtract indices and add to result
        # if lesser then add to the stack

        stack, res = [], [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
            
            if temperatures[i] < stack[-1][0]:
                stack.append([temperatures[i], i])
        
        return res
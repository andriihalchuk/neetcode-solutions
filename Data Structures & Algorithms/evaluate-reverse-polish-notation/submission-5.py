class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for t in tokens:
            if t.lstrip('-').isnumeric():
                evalStack.append(t)
            else:
                val1 = evalStack.pop()
                val2 = evalStack.pop()
                evalStack.append(str(int(eval(val2 + t + val1))))
            
        return round(float(evalStack.pop()))
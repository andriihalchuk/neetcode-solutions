class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', ']' : '[', '}': '{'}
        parStack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                parStack.append(bracket)
            elif not parStack or mapping[bracket] != parStack[-1]:
                return False
            else:
                parStack.pop()
            
        return not parStack
            
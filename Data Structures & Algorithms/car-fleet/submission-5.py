class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        mapping = [[pos, spd] for pos, spd in zip(position, speed)]
                
        for pos, spd in sorted(mapping)[::-1]:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            
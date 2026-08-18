class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        mapping = [[pos, spd] for pos, spd in zip(position, speed)]
        mapping = reversed(sorted(mapping))
                
        for i, car in enumerate(mapping):
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            
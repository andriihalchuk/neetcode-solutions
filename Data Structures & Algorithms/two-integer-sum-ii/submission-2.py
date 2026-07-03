class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i != j:
            numSum = numbers[i] + numbers[j]
            if numSum == target:
                return [i + 1, j + 1]
            elif numSum > target:
                j -= 1
            else:
                i += 1
            print(i, j)
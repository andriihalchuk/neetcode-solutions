class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        for row in matrix:
            if row[l] <= target <= row[r]:
                while l <= r:
                    mid = l + (r - l) // 2
                    if row[mid] < target:
                        l = mid + 1
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        return True

            else:
                continue
        return False
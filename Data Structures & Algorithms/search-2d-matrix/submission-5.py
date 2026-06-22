#Binary Search - O(log(m * n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        rows, col = len(matrix), len(matrix[0])
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        l, r = 0, col - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
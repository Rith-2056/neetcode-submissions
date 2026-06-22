#Binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
                                                                                                                                                                                     
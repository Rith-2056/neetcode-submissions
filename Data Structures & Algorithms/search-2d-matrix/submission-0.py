#Brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            for num in array:
                if num == target:
                    return True
        return False
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    seen.add((r,c))
        for r,c in seen:
            for i in range(cols):
                matrix[r][i] = 0
            for j in range(rows):
                matrix[j][c] = 0
            
        
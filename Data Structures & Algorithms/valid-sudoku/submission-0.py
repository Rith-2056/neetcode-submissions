#Brute force
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] in seen:
                    return False
                elif board[row][i] == '.':
                    continue
                else:
                    seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] in seen:
                    return False
                elif board[j][col] == '.':
                    continue
                else:
                    seen.add(board[j][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])      
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows, check columns, check 3x3 squares
        for row in range(9):
            seenRow = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                elif board[row][j] in seenRow:
                    return False
                else:
                    seenRow.add(board[row][j])
        for col in range(9):
            seenCol = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                elif board[j][col] in seenCol:
                    return False
                else:
                    seenCol.add(board[j][col])
        for squares in range(9):
            seenSquare = set()
            for i in range(3):
                for j in range(3):
                    row = (squares // 3) * 3 + i
                    col = (squares %3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seenSquare:
                        return False
                    seenSquare.add(board[row][col])
        return True
        
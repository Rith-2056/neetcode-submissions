#bfs implementation
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = collections.deque()
        visit = set()
        
        def bfs(r,c):
            q.append([r,c])
            visit.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = dr + r, dc + c
                    if 0 <=row<= rows - 1 and 0 <= col <= cols - 1 and board[row][col] == 'O' and (row,col) not in visit:
                        visit.add((row,col))
                        q.append([row,col])


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    bfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c] = 'X'

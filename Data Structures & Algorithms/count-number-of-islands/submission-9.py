class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        q = collections.deque()
        visit = set()

        def bfs(r,c):
            q.append([r,c])
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc) not in visit and grid[nr][nc] == '1':
                        q.append([nr,nc])
                        visit.add((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        def bfs(r,c): 
            area = 1
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >=0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visit:
                        area += 1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return area


        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_area = max(max_area, bfs(r,c))
        return max_area
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea= 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0,-1], [0,1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                            area += 1
                            q.append((r,c))
                            visit.add((r,c))
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea
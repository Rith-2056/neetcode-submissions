class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        q = collections.deque()
        visit = set()
        fresh = 0
        def rot(r,c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or grid[r][c] == 2 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
            fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rot(r + 1,c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            if q:
                minutes += 1
        if fresh > 0:
            return -1
        return minutes
            
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        fresh = 0

        def rot(r,c):
            nonlocal fresh
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or grid[r][c] == 0:
                return
            visit.add((r,c))
            q.append((r,c))
            fresh -= 1
        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            if q:
                minutes += 1
        if fresh > 0:
            return -1
        return minutes


                
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        #can go to a call if the call has a height equal or lower
        def reachPacific(r,c):
            q = collections.deque()
            visit = set()
            q.append([r,c])
            visit.add((r,c))
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r,c = q.popleft()
                if r == 0 or c == 0:
                    return True
                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if (row in range(rows)) and (col in range(cols)) and heights[r][c] >= heights[row][col] and (row,col) not in visit: 
                        q.append([row,col])
                        visit.add((row,col))
            return False
        def reachAtlantic(r,c):
            q = collections.deque()
            visit = set()
            q.append([r,c])
            visit.add((r,c))
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                r,c = q.popleft()
                if r == rows - 1 or c == cols - 1:
                    return True
                for dr, dc in direction:
                    row, col = r + dr, c + dc
                    if (row in range(rows)) and (col in range(cols)) and heights[r][c] >= heights[row][col] and (row,col) not in visit: 
                        q.append([row,col])
                        visit.add((row,col))
            return False
        


        for r in range(rows):
            for c in range(cols):
                if reachPacific(r,c) and reachAtlantic(r,c):
                    res.append([r,c])
        return res
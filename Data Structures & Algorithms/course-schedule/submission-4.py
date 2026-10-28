class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #input: numCourses = 2
        #adjList = [[], []]
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * (numCourses)

        for crs, preq in prerequisites:
            adj[preq].append(crs)
            indegree[crs] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for nxtCrs in adj[course]:
                indegree[nxtCrs] -= 1
                if indegree[nxtCrs] == 0:
                    q.append(nxtCrs)
        return completed == numCourses
        

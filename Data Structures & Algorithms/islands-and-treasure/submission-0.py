class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        r,c = len(grid),len(grid[0])
        visit = set()
        queue = collections.deque()

        def addNode(r1,c1):
            if 0<=r1<r and 0<=c1<c and grid[r1][c1] != -1 and (r1,c1) not in visit:
                visit.add((r1,c1))
                queue.append((r1,c1))

        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append((i,j))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r2,c2 = queue.popleft()
                grid[r2][c2] = dist
                addNode(r2+1,c2)
                addNode(r2-1,c2)
                addNode(r2,c2+1)
                addNode(r2,c2-1)
            dist+=1

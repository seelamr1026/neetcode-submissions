class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        r,c = len(grid),len(grid[0])
        visit = set()
        queue = collections.deque()

        def addNode(r2,c2):
            if 0<=r2<r and 0<=c2<c and grid[r2][c2] != -1 and (r2,c2) not in visit:
                visit.add((r2,c2))
                queue.append((r2,c2))


        for i in range(0,r): 
            for j in range(0,c):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append((i,j))
        
        dist = 0
        while queue:
            for _ in range(0,len(queue)):
                r1,c1 = queue.popleft()
                grid[r1][c1] = dist
                addNode(r1+1,c1)
                addNode(r1-1,c1)
                addNode(r1,c1+1)
                addNode(r1,c1-1)
            dist+=1
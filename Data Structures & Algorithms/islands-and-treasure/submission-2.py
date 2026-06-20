class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        r,c = len(grid),len(grid[0])
        queue = collections.deque()
        visit = set()

        def addNode(row,col):
            if 0<=row<r and 0<=col<c and grid[row][col] != -1 and (row,col) not in visit:
                visit.add((row,col))
                queue.append((row,col))

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


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        row,col = len(grid),len(grid[0])
        area = 0
        queue = collections.deque()
        visited = set()

        def bfs(i,j):
            visited.add((i,j))
            queue.append([i,j])
            currarea = 1

            while queue:
                x,y = queue.popleft()
                for dr,dc in directions:
                    i1,j1 = x+dr,y+dc
                    if i1>=0 and i1<row and j1>=0 and j1<col and grid[i1][j1] == 1 and (i1,j1) not in visited:
                        currarea+=1
                        visited.add((i1,j1))
                        queue.append([i1,j1])
            
            return currarea




        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    tempArea = bfs(i,j)
                    area = max(area,tempArea)

        return area
        
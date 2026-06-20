class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        r,c = len(grid),len(grid[0])
        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = collections.deque()
        visited = set()


        def bfs(r1,c1) -> int:
            count = 1
            queue.append((r1,c1))
            visited.add((r1,c1))
            while queue:
                r2,c2 = queue.popleft()
                #print(count)
                for j,k in movement:
                    row,column = r2+j, c2+k
                    if row>= 0 and row < r and column >=0 and column < c and grid[row][column] == 1 and (row,column) not in visited:
                        queue.append((row,column))
                        visited.add((row,column))
                        count+=1
            
            return count



        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = max(area,bfs(i,j))
        

        return area
        
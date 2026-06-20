class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        count = 0
        movement = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = collections.deque()
        visited = set()
        r,c = len(grid),len(grid[0])

        # basecase

        if r==0 and c ==0:
            return 0
        
        def bfs (row,column):
            queue.append((row,column))
            visited.add((row,column))

            while queue:
                r1,c1 = queue.popleft()
                for x,y in movement:
                    row1,col1 = r1+x,c1+y
                    if row1>=0 and row1<r and col1>=0 and col1<c and grid[row1][col1] == "1" and (row1,col1) not in visited:
                        queue.append((row1,col1))
                        visited.add((row1,col1))

        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count+=1
                    bfs(i,j)
        

        return count

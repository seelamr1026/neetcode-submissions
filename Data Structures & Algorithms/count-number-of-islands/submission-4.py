class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        movement = [[-1,0],[1,0],[0,1],[0,-1]]
        row,col = len(grid),len(grid[0])
        count = 0

        def dfs(i,j):
            
            if (i<0 or i>= row or j<0 or j>=col or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            for x,y in movement:
                dfs(i+x,j+y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1

        return count
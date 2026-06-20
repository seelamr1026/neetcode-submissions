class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:

        pac = set()
        alt = set()
        r,c = len(grid),len(grid[0])

        def dfs(row,col,visit,preVal):

            if row<0 or row==r or col<0 or col==c or (row,col) in visit or grid[row][col]<preVal:
                return
            
            visit.add((row,col))
            dfs(row+1,col,visit,grid[row][col])
            dfs(row-1,col,visit,grid[row][col])
            dfs(row,col+1,visit,grid[row][col])
            dfs(row,col-1,visit,grid[row][col])


        for j in range(c):
            dfs(0,j,pac,grid[0][j])
            dfs(r-1,j,alt,grid[r-1][j])
        
        for i in range(r):
            dfs(i,0,pac,grid[i][0])
            dfs(i,c-1,alt,grid[i][c-1])

        res = []
        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        

        return res
        
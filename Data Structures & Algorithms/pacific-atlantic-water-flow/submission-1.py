class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r,c= len(heights),len(heights[0])
        pac,alt = set(),set()

        def dfs(row,col,visit,prevVal):
            if (row,col) in visit or row<0 or col<0 or row==r or c==col or heights[row][col]<prevVal:
                return
            
            visit.add((row,col))

            dfs(row+1,col,visit,heights[row][col])
            dfs(row-1,col,visit,heights[row][col])
            dfs(row,col-1,visit,heights[row][col])
            dfs(row,col+1,visit,heights[row][col])


        for j in range(c):
            dfs(0,j,pac,heights[0][j])
            dfs(r-1,j,alt,heights[r-1][j])
        
        for i in range(r):
            dfs(i,0,pac,heights[i][0])
            dfs(i,c-1,alt,heights[i][c-1])
        
        res = []

        for i in range(r):
            for j in range(c):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        
        return res

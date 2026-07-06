class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        count = 0
        row,col = len(grid),len(grid[0])
        visited = set()
        queue = collections.deque()

        if row == 0 and col == 0:
            return 0

        def bfs(i,j):
            visited.add((i,j))
            queue.append([i,j])

            while queue:
                i1,j1 = queue.popleft()
                for x,y in directions:
                    r,c = i1+x,j1+y
                    if r>=0 and r<row and c>=0 and c<col and (r,c) not in visited and grid[r][c] == "1":
                        visited.add((r,c))
                        queue.append([r,c])



        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1" and (i,j) not in visited:
                    count+=1
                    bfs(i,j)
        
        return count


        
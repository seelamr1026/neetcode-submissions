class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        movement = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        queue = collections.deque()
        r,c = len(grid),len(grid[0])

        if r==0 and c==0:
            return 0

        def bfs(row,column):
            visited.add((row,column))
            queue.append((row,column))

            while(queue):
                r1,c1 = queue.popleft()
                for j,k in movement:
                    r2,c2=r1+j,c1+k
                    if r2>=0 and r2<r and c2>=0 and c2<c and grid[r2][c2] == "1" and (r2,c2) not in visited:
                        queue.append((r2,c2))
                        visited.add((r2,c2))

        for i in range(0,r):
            for j in range(0,c):

                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count+=1

        return count
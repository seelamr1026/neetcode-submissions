class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r,c = len(grid),len(grid[0])
        queue = collections.deque()
        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        minute = 0

        fresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while fresh>0 and queue:
            for _ in range(len(queue)):
                r1,c1 = queue.popleft()
                for x,y in movement:
                    row,col = r1+x,c1+y
                    if 0<=row<r and 0<=col<c and grid[row][col]==1:
                        queue.append((row,col))
                        grid[row][col] = 2
                        fresh-=1
            minute+=1

        return minute if fresh==0 else -1
        
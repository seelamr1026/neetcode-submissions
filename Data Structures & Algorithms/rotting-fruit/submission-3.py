class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r,c = len(grid),len(grid[0])
        visit = set()
        queue = collections.deque()
        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        minute = 0

        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        while fresh>0 and queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for r1,c1 in movement:
                    row,col = x+r1,y+c1
                    if 0<=row<r and 0<=col<c and grid[row][col] == 1 and (row,col) not in visit:
                        queue.append((row,col))
                        visit.add((row,col))
                        grid[row][col] = 2
                        fresh-=1
            minute+=1
        
        return minute if fresh == 0 else -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r,c = len(grid),len(grid[0])
        movement = [[-1,0],[1,0],[0,-1],[0,1]]
        queue = collections.deque()
        fresh = 0

        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        minute = 0
        print(fresh)
        while fresh >0 and queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                for x,y in movement:
                    r1,c1 = row+x,col+y
                    if 0<=r1<r and 0<=c1<c and grid[r1][c1] == 1:
                        grid[r1][c1] = 2
                        queue.append((r1,c1))
                        fresh-=1
            minute+=1

        print(fresh)
        return minute if fresh == 0 else -1



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        movement = [[-1,0],[1,0],[0,-1],[0,1]]
        r,c = len(grid),len(grid[0])
        queue = collections.deque()
        visited = set()
        area = 0

        if r == 0 and c == 0:
            return 0

        def bfs(row,col) -> int:
            count = 1
            queue.append((row,col))
            visited.add((row,col))

            while(queue):
                r1,c1 = queue.popleft()
                for x,y in movement:
                    r2,c2 = r1+x,c1+y
                    if r2>=0 and r2<r and c2>=0 and c2<c and grid[r2][c2] == 1 and (r2,c2) not in visited:
                        count+=1
                        visited.add((r2,c2))
                        queue.append((r2,c2))
            
            return count


        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = max(area,bfs(i,j))
        
        return area
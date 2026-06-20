class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dpArr = [[0]*(n+1) for _ in range(m+1)]
        dpArr[m-1][n-1] = 1

        for i in range (m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dpArr[i][j] += dpArr[i+1][j] + dpArr[i][j+1]
        
        return dpArr[0][0]
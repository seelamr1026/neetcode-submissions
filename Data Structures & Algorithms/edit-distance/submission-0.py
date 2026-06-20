class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dpArr = [[0]*(n+1) for _ in range (m+1)]

        for i in range(1,m+1):
            dpArr[i][0] = i
        
        for i in range(1,n+1):
            dpArr[0][i] = i
        
        for i in range (1,m+1):
            for j in range (1,n+1):
                if word1[i-1] == word2[j-1]:
                    dpArr[i][j] = dpArr[i-1][j-1]
                else:
                    dpArr[i][j] = 1+ min(dpArr[i-1][j],dpArr[i][j-1],dpArr[i-1][j-1])
        
        return dpArr[m][n]
        
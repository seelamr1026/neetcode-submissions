class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1),len(text2)

        dpArr = [[0]*n for _ in range(m)]

        if text1[0] == text2[0]:
            dpArr[0][0] = 1

        for i in range(1,n):
            if text2[0] == text1[i]:
                dpArr[0][i] = max(dpArr[0][i-1],1)
            else:
                dpArr[0][i] = dpArr[0][i-1]
        for j in range(1,m):
            if text2[j] == text1[0]:
                dpArr[j][0] = max(dpArr[j-1][0],1)
            else:
                dpArr[j][0] = dpArr[j-1][0]

        print(dpArr)

        for i in range(1,m):
            for j in range(1,n):
                if text1[j] == text2[i]:
                    dpArr[i][j] += 1+ dpArr[i-1][j-1]
                else:
                    dpArr[i][j] = max(dpArr[i-1][j],dpArr[i][j-1])
        
        return dpArr[m-1][n-1]

        
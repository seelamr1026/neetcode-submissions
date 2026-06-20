class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n, m = len(text1),len(text2)
        dpArr = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text2[i] == text1[j]:
                    dpArr[i][j] = 1+dpArr[i+1][j+1]
                else:
                    dpArr[i][j] = max(dpArr[i+1][j],dpArr[i][j+1])
        print(dpArr)
        return dpArr[0][0]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dpArr = [False]*(n+1)
        dpArr[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                if i+len(w)<=n and s[i:i+len(w)] == w:
                    dpArr[i] = dpArr[i+len(w)]
                if dpArr[i]:
                    break
        
        return dpArr[0]
        
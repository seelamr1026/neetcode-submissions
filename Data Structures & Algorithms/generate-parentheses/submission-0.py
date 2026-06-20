class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(openC,closeC,string):
            if len(string) == n*2 and openC == closeC:
                    res.append(string)
                    return
            

            if len(string)== 0 or openC <n:
                backtrack(openC+1,closeC,string+"(")
            
            if closeC < openC:
                backtrack(openC,closeC+1,string+")")
        
        backtrack(0,0,"")
        return res
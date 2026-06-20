class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort()

        def dfs(i,subarr,total):
            #base case 1: if total is equal to target, add to the res array
            if total == target:
                res.append(subarr.copy())
                return
            #base case 2: if total is greater than target or pointer is over the bounds, return
            if total>target or i>=len(candidates):
                return
            
            #case 1 : include the element and increase the pointer
            subarr.append(candidates[i])
            dfs(i+1,subarr,total+candidates[i])
            subarr.pop()
            #case 2: not include the pointer and skip all the common elements and edge cases
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,subarr,total)
            

        dfs(0,[],0)
        return res
        
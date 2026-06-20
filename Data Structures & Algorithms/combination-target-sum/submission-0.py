class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        
        def dfs(sum,i,subset):

            if sum == target:
                res.append(subset.copy())
                return

            if sum > target or i>=len(nums):
                return
            
            subset.append(nums[i])
            dfs(sum + nums[i], i, subset)
            subset.pop()
            dfs(sum, i + 1, subset)
        
        dfs(0,0,[])
        return res

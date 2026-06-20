class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        # to store the final results
        subset = []
        # to store the intermedaite results

        def dfs(i):

            #base class
            if i>= len(nums):
                res.append(subset.copy())
                # in python u always take copy of the subset as you are performing operations on the same variable
                return
            
            #decision to include
            subset.append(nums[i])
            dfs(i+1)
            #decision to remove
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res


    

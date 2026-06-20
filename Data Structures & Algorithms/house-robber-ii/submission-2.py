class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)

        def helper(arr):
            
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            
            res = [0]*len(arr)
            res[0] = arr[0]
            res[1] = max(arr[0],arr[1])

            for i in range(2,len(arr)):
                res[i] = max(res[i-2]+arr[i],res[i-1])
            
            return res[len(arr)-1]

        return max(helper(nums[1:]),helper(nums[:-1]))
        
class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        res = [0]*len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            res[i] = max(nums[i]+res[i-2],res[i-1])
        
        return res[len(nums)-1]
        
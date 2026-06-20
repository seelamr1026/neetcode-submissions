class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sums = 0
        for num in nums:
            sums+=num
        
        if sums%2 != 0:
            return False
        
        sums = sums//2
        memory = [[False]*(sums+1) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            memory[i][0] = True
        
        for i in range(1,len(nums)+1):
            for j in range(1,sums+1):
                if nums[i-1] <= j:
                    memory[i][j] = memory[i-1][j] or memory[i-1][j-nums[i-1]]
                else:
                    memory[i][j] = memory[i-1][j]
        
        return memory[len(nums)][sums]


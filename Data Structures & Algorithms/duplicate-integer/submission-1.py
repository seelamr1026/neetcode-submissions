class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        matchingset = set()

        for num in nums:
            matchingset.add(num)
        
        if len(nums) != len(matchingset):
            return True
        
        return False
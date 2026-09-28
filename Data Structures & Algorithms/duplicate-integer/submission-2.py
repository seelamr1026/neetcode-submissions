class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numset = set()

        for i in nums:
            numset.add(i)
        
        if len(numset) == len(nums):
            return False
        return True
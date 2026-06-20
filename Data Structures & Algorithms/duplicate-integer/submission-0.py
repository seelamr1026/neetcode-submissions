class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        repeated = set()

        for num in nums:
            if num in repeated:
                return True
            else:
                repeated.add(num)
        
        return False
        
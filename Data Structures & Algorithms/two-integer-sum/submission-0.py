class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_index = {}

        for i in range(0,len(nums)):
            if target-nums[i] in map_index:
                return [map_index[target-nums[i]],i]
            else:
                map_index[nums[i]]=i
         
        
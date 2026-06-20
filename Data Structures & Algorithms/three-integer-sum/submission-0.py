class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = list([])
        nums.sort()
        def recurse(temp,totalsum,i):
            if len(temp) == 3:
                print(temp,totalsum)
                if totalsum == 0:
                    result.append(temp.copy())
                    return
                else:
                    return
            elif len(temp)>3:
                return
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                temp.append(nums[j])
                totalsum+=nums[j]
                recurse(temp,totalsum,j+1)
                temp.pop()
                totalsum-=nums[j]
        
        recurse([],0,0)
        return result
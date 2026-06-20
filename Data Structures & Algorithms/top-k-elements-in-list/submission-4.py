class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        if len(nums)==0:
            return []
        res = list([])
        i=0
        count = 1
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                count+=1
            else:
                res.append([count,nums[i]])
                count = 1
            i+=1
        res.append([count,nums[i]])
        res = sorted(res,reverse=True)
        print(res)
        counter = 0
        final = []
        while counter<k:
            final.append(res[counter][1])
            counter+=1
        print(final)


        return final

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        storingarr = defaultdict(int)
        result = []

        for num in nums:
            if num not in storingarr.keys():
                storingarr[num] = 1
            else:
                storingarr[num]+=1
        
        sorted_arr = {key:value for key,value in sorted(storingarr.items(),key=lambda item: item[1],reverse = True)}

        print(sorted_arr)
        
        for i in sorted_arr:
            result.append(i)
        
        print(result[:k])
        return result[:k]


        
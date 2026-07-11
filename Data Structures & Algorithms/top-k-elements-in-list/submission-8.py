class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencyMap = defaultdict(int)

        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 1
            else:
                frequencyMap[num] += 1
        
        frequencyMap = {key: value for key,value in sorted(frequencyMap.items(),key=lambda item:item[1], reverse = True)}

        finalArr = []

        for finalK in frequencyMap.keys():
            finalArr.append(finalK)
        
        return finalArr[:k]


        
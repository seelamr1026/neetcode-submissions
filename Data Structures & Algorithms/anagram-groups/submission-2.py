class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[""]]
        
        finalmap  = defaultdict(list)

        for word in strs :
            sorted_word = ''.join(sorted(word))
            finalmap[sorted_word].append(word)
        
        result = []

        for arr in finalmap:
            print(arr)
            result.append(finalmap[arr])
        
        return result
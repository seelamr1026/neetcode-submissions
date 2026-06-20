class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_index = defaultdict(list)
        result = []

        for st in strs:
            sorted_st = ''.join(sorted(st))
            map_index[sorted_st].append(st)
        
        for ind in map_index:
            result.append(map_index[ind])

        return result        
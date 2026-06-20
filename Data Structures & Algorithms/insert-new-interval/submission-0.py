class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:

        res = []
        n = len(intervals)
        i = 0

        while i<n and intervals[i][1] < newinterval[0]:
            res.append(intervals[i])
            i+=1
        
        while i<n and newinterval[1] >= intervals[i][0]:
            newinterval[0] = min(intervals[i][0],newinterval[0])
            newinterval[1] = max(intervals[i][1],newinterval[1])
            i+=1
        res.append(newinterval)
        while(i<n):
            res.append(intervals[i])
            i+=1
        return res
        
        
        
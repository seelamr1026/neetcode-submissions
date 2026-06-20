class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        start = 0
        end = len(heights)-1
        while(start<end):
            currentWater = min(heights[start],heights[end])*(end-start)
            maxWater = max(maxWater,currentWater)
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        
        return maxWater
        
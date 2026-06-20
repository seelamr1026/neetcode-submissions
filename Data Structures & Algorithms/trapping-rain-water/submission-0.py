class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        start,end = 0,len(height)-1
        res = 0
        leftMax,rightMax = height[start],height[end]
        while start<end:
            if leftMax<rightMax:
                start+=1
                leftMax = max(leftMax,height[start])
                res+=leftMax-height[start]
            else:
                end-=1
                rightMax = max(rightMax,height[end])
                res+=rightMax-height[end]
        
        return res

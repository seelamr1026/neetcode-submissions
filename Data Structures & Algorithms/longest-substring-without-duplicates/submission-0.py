class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left,right,maxLen = 0,0,0
        visited = set()

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            visited.add(s[right])
            maxLen = max(maxLen,(right-left+1))
        
        return maxLen
        
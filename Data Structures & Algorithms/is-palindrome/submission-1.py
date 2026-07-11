class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for char in s:
            if char.isalnum():
                c+=char.lower()
        
        return c == c[::-1]
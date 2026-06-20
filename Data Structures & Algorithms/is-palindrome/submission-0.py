class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for char in s:
            if char.isalnum():
                c+=char.lower()
        
        reversec = c[::-1]
        print(c,reversec)
        return True if c==reversec else False
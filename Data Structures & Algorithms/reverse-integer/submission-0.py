class Solution:
    def reverse(self, x: int) -> int:
        original = x
        x = abs(x)

        reverse = str(x)[::-1]
        reverseint = int(reverse)

        if original < 0:
            reverseint*=-1
        
        if -2**31 -1 < reverseint < 2**31-1:
            return reverseint
        return 0
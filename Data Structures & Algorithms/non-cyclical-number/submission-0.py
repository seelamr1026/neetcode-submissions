class Solution:
    def isHappy(self, n: int) -> bool:

        visit = set()

        while (1):
            strn = str(n)
            square = 0
            for i in strn:
                square+=int(i)**2
            if square == 1:
                return True
            elif square not in visit:
                visit.add(square)
                n=square
            else:
                return False


        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1 = len(s1)
        l2 = len(s2)
        set1 = sorted(s1)

        for i in range(0,l2):
            if s2[i] in s1:
                set2 = sorted(s2[i:i+l1])
                if set1 == set2:
                    return True
        
        return False

        
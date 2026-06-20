class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo,hi = 1, max(piles)

        while lo<hi:
            mid = (lo+hi)//2

            time = sum(math.ceil(p/mid) for p in piles)
            
            if time<=h:
                hi = mid
            if time >h:
                lo = mid+1
        
        return lo

        
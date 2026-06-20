class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        lo,hi = 0, m*n -1

        while lo<=hi:
            mid = (lo+hi)//2
            row,col = divmod(mid,n)
            val = matrix[row][col]

            if val == target:
                return True
            if val<target:
                lo = mid+1
            if val> target:
                hi = mid-1

        return False        
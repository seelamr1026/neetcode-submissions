class Solution:
    def solve(self, board: List[List[str]]) -> None:

        r,c = len(board),len(board[0])

        def surround(row,col):

            if row<0 or col<0 or row==r or col==c or board[row][col] != "O":
                return

            board[row][col] = "T"

            surround(row+1,col)
            surround(row-1,col)
            surround(row,col-1)
            surround(row,col+1)

        for j in range(c):
            surround(0,j)
            surround(r-1,j)

        for i in range(r):
            surround(i,0)
            surround(i,c-1)


        for i in range(r):
            for j in range(c):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"        


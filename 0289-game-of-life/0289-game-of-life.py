class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]

        m=len(board)
        n=len(board[0])

        for x in range(m):
            for y in range(n):
                count=0
                for dx,dy in neighbors:
                    if 0<=x+dx < m and 0<=y+dy < n:
                        count+=board[x+dx][y+dy] & 1

                if board[x][y]==1 and 2<=count<=3:
                    board[x][y]=3
                elif board[x][y]==0 and count==3:
                    board[x][y]=2

        for x in range(m):
            for y in range(n):
                board[x][y] >>= 1
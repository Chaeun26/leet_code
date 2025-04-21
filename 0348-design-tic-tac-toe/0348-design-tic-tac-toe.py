class TicTacToe:

    def __init__(self, n: int):
        self.n=n
        self.board=[[0]*(n) for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col]=player
        horizontal=vertical=diagonal1=diagonal2=player

        for i in range(self.n):
            horizontal &= self.board[i][col]
        for j in range(self.n):
            vertical &= self.board[row][j]

        if row==col or row+col==self.n-1:
            sRow,sCol=0,self.n-1
            for i in range(self.n):
                diagonal1 &= self.board[sRow][sRow]
                diagonal2 &= self.board[sRow][sCol]
                sRow+=1
                sCol-=1
            return horizontal or vertical or diagonal1 or diagonal2

        return horizontal or vertical


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
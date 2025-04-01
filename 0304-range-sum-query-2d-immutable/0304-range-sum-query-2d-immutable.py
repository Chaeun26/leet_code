class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n=len(matrix),len(matrix[0])
        self.prefix_sum = matrix[:]

        for r in range(1,m):
            self.prefix_sum[r][0] += self.prefix_sum[r-1][0]
        
        for c in range(1,n):
            self.prefix_sum[0][c] += self.prefix_sum[0][c-1]
        
        for r in range(1,m):
            for c in range(1,n):
                self.prefix_sum[r][c] += self.prefix_sum[r-1][c] + self.prefix_sum[r][c-1] - self.prefix_sum[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a=b=c=0

        if col1-1>=0:
            a = self.prefix_sum[row2][col1-1]
        if row1-1>=0:
            b = self.prefix_sum[row1-1][col2]
        if row1-1>=0 and col1-1>=0:
            c = self.prefix_sum[row1-1][col1-1]
        
        return self.prefix_sum[row2][col2] - a - b + c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
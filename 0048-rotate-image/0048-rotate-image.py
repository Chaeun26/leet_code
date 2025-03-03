class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n=len(matrix)
        # tmp = [[0]*n for _ in range(n)]

        # for r in range(n):
        #     for c in range(n):
        #         tmp[c][n-r-1] = matrix[r][c]

        # matrix[:]=tmp
        self.transpose(matrix)
        self.reflect(matrix)


    def transpose(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i],matrix[i][j] = matrix[i][j], matrix[j][i]
    
    def reflect(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]



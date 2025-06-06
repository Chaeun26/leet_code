class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row = any(matrix[0][c]==0 for c in range(n))
        first_col = any(matrix[r][0]==0 for r in range(m))

        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0

        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        if first_row:
            for c in range(n):
                matrix[0][c]=0
        if first_col:
            for r in range(m):
                matrix[r][0]=0

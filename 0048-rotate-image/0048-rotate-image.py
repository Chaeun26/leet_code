class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        tmp = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                tmp[c][n-r-1] = matrix[r][c]

        matrix[:]=tmp
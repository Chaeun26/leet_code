class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])

        count=[[0]*n for _ in range(m)]
        ans=0
        for r in range(m):
            for c in range(n):
                if matrix[r][c]=="1":
                    count[r][c]=min(count[r-1][c],count[r][c-1],count[r-1][c-1])+1
                    ans=max(ans, count[r][c])
        return ans*ans

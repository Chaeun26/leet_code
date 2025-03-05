class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])

        dp=mat[:]

        for r in range(m):
            for c in range(n):
                min_neighbor=inf
                if dp[r][c]!=0:
                    if r>0:
                        min_neighbor=min(min_neighbor,dp[r-1][c])
                    if c>0:
                        min_neighbor=min(min_neighbor,dp[r][c-1])
                    dp[r][c]=min_neighbor+1

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                min_neighbor=inf
                if dp[r][c]!=0:
                    if r<m-1:
                        min_neighbor=min(min_neighbor,dp[r+1][c])
                    if c<n-1:
                        min_neighbor=min(min_neighbor,dp[r][c+1])
                    dp[r][c]=min(dp[r][c],min_neighbor+1)
        
        return dp

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m,n=len(grid),len(grid[0])
        ans=0
        dp=[[0]*n for _ in range(m)]
        dp2=[[False]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="X":
                    grid[r][c]=1
                    dp2[r][c]=True
                elif grid[r][c]=="Y":
                    grid[r][c]=-1
                else:
                    grid[r][c]=0
                
                dp[r][c]=grid[r][c]

                if r==0 and c>0:
                    dp[r][c]+=dp[r][c-1]
                    dp2[r][c]=dp2[r][c] or dp2[r][c-1]
                elif c==0 and r>0:
                    dp[r][c]+=dp[r-1][c]
                    dp2[r][c]=dp2[r][c] or dp2[r-1][c]
                elif r>0 and c>0:
                    dp[r][c]+=dp[r-1][c]+dp[r][c-1]-dp[r-1][c-1]
                    dp2[r][c]=dp2[r][c] or dp2[r-1][c] or dp2[r][c-1]

                if dp[r][c]==0 and dp2[r][c]:
                    ans+=1

        return ans
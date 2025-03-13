class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m,n=len(grid),len(grid[0])
        ans=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="X":
                    grid[r][c]=1
                elif grid[r][c]=="Y":
                    grid[r][c]=-1
                else:
                    grid[r][c]=0

        col_sum=[0]*n
        is_contain=[False]*n
        for r in range(m):
            for c in range(n):
                col_sum[c]+=grid[r][c]
                if grid[r][c]==1:
                    is_contain[c]=True

            prefix_sum=0
            for c in range(n):
                prefix_sum+=col_sum[c]
                if prefix_sum==0:
                    for i in range(c+1):
                        if is_contain[i]:
                            ans+=1
                            break

        return ans
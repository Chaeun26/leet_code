class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        
        ans=0
        rowE=0
        colE=[0]*n
        
        for r in range(m):
            for c in range(n):
                if c==0 or grid[r][c-1]=="W":
                    rowE=0
                    for i in range(c,n):
                        if grid[r][i]=="W":
                            break
                        elif grid[r][i]=="E":
                            rowE+=1
                
                if r==0 or grid[r-1][c]=="W":
                    colE[c]=0
                    for i in range(r,m):
                        if grid[i][c]=="W":
                            break
                        elif grid[i][c]=="E":
                            colE[c]+=1
                
                if grid[r][c]=="0":
                    ans=max(ans,rowE+colE[c])
        
        return ans
                    
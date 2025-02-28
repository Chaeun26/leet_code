class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        ans=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    grid[r][c]="0"
                    ans+=1

                    stack=[(r,c)]
                    while stack:
                        x,y=stack.pop()

                        for dx,dy in directions:
                            if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]=="1":
                                grid[x+dx][y+dy]="0"
                                stack.append((x+dx,y+dy))
        
            
        return ans
            
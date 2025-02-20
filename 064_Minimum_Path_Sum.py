class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if r-1>=0 and c-1>=0:
                    grid[r][c]+=min(grid[r-1][c], grid[r][c-1])
                elif r-1>=0:
                    grid[r][c]+=grid[r-1][c]
                elif c-1>=0:
                    grid[r][c]+=grid[r][c-1]
        
        return grid[m-1][n-1]

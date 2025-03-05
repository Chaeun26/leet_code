class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        
        rows={r:[0,0] for r in range(m)}
        cols={c:[0,0] for c in range(n)}

        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    rows[r][0]+=1
                    cols[c][0]+=1
                else:
                    rows[r][1]+=1
                    cols[c][1]+=1

        for r in range(m):
            for c in range(n):
                grid[r][c] = rows[r][1]+cols[c][1]-rows[r][0]-cols[c][0]

        return grid
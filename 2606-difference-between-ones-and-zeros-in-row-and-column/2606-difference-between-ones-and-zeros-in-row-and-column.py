class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        
        # rows={r:[0,0] for r in range(m)}
        row_0=[0]*m
        row_1=[0]*m
        # cols={c:[0,0] for c in range(n)}
        col_0=[0]*n
        col_1=[0]*n


        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    # rows[r][0]+=1
                    # cols[c][0]+=1
                    row_0[r]+=1
                    col_0[c]+=1
                else:
                    # rows[r][1]+=1
                    # cols[c][1]+=1
                    row_1[r]+=1
                    col_1[c]+=1

        for r in range(m):
            for c in range(n):
                # grid[r][c] = rows[r][1]+cols[c][1]-rows[r][0]-cols[c][0]
                grid[r][c] = row_1[r]+col_1[c]-row_0[r]-col_0[c]

        return grid
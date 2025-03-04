class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0

        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        if m==1 and n==1:
            return 1
        elif m==2 and n==1:
            return 1 if obstacleGrid[0][0]==0 and obstacleGrid[1][0]==0 else 0
        elif m==1 and n==2:
            return 1 if obstacleGrid[0][0]==0 and obstacleGrid[0][1]==0 else 0

        path=[[0]*(n+1) for _ in range(m+1)]

        path[1][1]=1

        for r in range(1,m+1):
            for c in range(1,n+1):
                if obstacleGrid[r-1][c-1]!=1:
                    path[r][c]+=path[r-1][c]+path[r][c-1]

        return path[m][n]
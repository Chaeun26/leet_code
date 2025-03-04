class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0

        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        obstacleGrid[0][0]=1

        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0]== 0 and obstacleGrid[i-1][0]==1)

        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j]==0 and obstacleGrid[0][j-1]==1)

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1])
                else:
                    obstacleGrid[i][j]=0
        
        return obstacleGrid[m-1][n-1]

        # if m==1 and n==1:
        #     return 1
        # elif m==2 and n==1:
        #     return 1 if obstacleGrid[0][0]==0 and obstacleGrid[1][0]==0 else 0
        # elif m==1 and n==2:
        #     return 1 if obstacleGrid[0][0]==0 and obstacleGrid[0][1]==0 else 0

        # path=[[0]*(n+1) for _ in range(m+1)]

        # path[1][1]=1

        # for r in range(1,m+1):
        #     for c in range(1,n+1):
        #         if obstacleGrid[r-1][c-1]!=1:
        #             path[r][c]+=path[r-1][c]+path[r][c-1]

        # return path[m][n]
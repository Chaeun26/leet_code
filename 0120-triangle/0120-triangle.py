class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]

        dp = triangle[:]

        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j-1 >= 0 and j<len(triangle[i-1]):
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])
                elif j-1 < 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j-1]

        ans=float('inf')
        for j in range(len(triangle[-1])):
            ans = min(ans,dp[len(triangle[-1])-1][j])

        return ans
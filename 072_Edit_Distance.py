class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))

        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):

                dp[i][0] = i
                dp[0][j] = j
                
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

        return dp[len(word1)][len(word2)]

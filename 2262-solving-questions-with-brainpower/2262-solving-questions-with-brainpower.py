class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*n

        dp[n-1]=questions[n-1][0]

        for i in range(n-2,-1,-1):
            point, brainpower = questions[i]
            
            if i+brainpower+1 < n:
                dp[i] = max(dp[i+brainpower+1]+point, dp[i+1])
            else:
                dp[i] = max(point, dp[i+1])
        
        return dp[0]
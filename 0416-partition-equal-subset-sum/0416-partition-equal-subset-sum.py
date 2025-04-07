class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=0
        res = False
        
        for n in nums:
            total_sum+=n
        
        if total_sum%2!=0:
            return res

        goal = total_sum//2
        dp = [False]*(goal+1)
        dp[0]=True
        
        for n in nums:
            for s in range(goal, n-1, -1):
                dp[s] = dp[s] or dp[s-n]

        return dp[goal]

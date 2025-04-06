class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)

        nums.sort()
        prev=[-1]*n
        dp=[1]*n
        max_idx=0

        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i] < dp[j] + 1:
                    prev[i]=j
                    dp[i]=dp[j]+1
                if dp[i] > dp[max_idx]:
                    max_idx = i

        res=[]
        k=max_idx
        while k>=0:
            res.append(nums[k])
            k=prev[k]

        return res
        '''
        # backtracking - TLE occurs

        n=len(nums)
        nums.sort()
        self.max_len=0
        self.res=[]
        
        def backtrack(idx,curr):
            if idx==n:
                if len(curr)>self.max_len:
                    self.max_len=len(curr)
                    self.res=curr[:]
                return 

            if not curr or nums[idx]%curr[-1]==0:
                curr.append(nums[idx])
                backtrack(idx+1, curr)
                curr.pop()

            backtrack(idx+1, curr)

        backtrack(0,[])
        return self.res
        '''
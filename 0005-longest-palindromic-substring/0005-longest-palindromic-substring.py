class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=1
        li=lj=0
        dp = [[False]*len(s) for _ in range(len(s))]

        dp[0][0]=True
        
        for i in range(len(s)-1):
            dp[i][i]=True
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                longest=2
                li=i
                lj=i+1
        

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                    if longest < j-i+1:
                        longest=j-i+1
                        li=i
                        lj=j

        return s[li:lj+1]
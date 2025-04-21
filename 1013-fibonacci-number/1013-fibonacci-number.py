class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        ans,prev=1,0

        for i in range(n-1):
            tmp=ans
            ans+=prev
            prev=tmp

        
        return ans

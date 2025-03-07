class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        y=abs(x)
        
        while y>0:
            ans = ans*10 + y%10
            y=y//10
            if ans>2**31:
                return 0
        
        return ans if x>0 else -ans
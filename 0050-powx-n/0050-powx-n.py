class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x,n):
            if n==0:
                return 1
            
            half = pow(x,n//2)

            if n%2==0:
                return half*half
            else:
                return half*half*x

        if n < 0:
            return 1/pow(x,-n)
        else:
            return pow(x,n)
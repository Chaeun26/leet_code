import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


# Newton's Method
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        x0=x
        x1=(x0+x/x0)/2
        while abs(x0-x1)>=1:
            x0=x1
            x1=(x0+float(x)/x0)/2

        return int(x1)

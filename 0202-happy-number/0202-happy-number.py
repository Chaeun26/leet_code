class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_all(n):
            total=0
            while n>0:
                digit=n%10
                total+=digit**2
                n//=10
            return total

        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=sum_all(n)
        
        return n==1
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7

        even_idx=(n+1)//2
        odd_idx=n//2
        
        return (pow(5, even_idx, mod) * pow(4, odd_idx, mod)) % mod
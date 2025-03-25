from itertools import combinations

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat_all_banana(k: int, piles: List[int]) -> bool:
            hrs=0
            for n in piles:
                hrs+=math.ceil(n/k)
            return hrs<=h
        
        left,right=1,max(piles)
        while left<right:
            mid=(left+right)//2
            if eat_all_banana(mid,piles):
                right=mid
            else:
                left=mid+1
        
        return left

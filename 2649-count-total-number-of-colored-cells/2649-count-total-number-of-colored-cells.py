class Solution:
    def coloredCells(self, n: int) -> int:
        ans=1
        
        for i in range(n,0,-1):
            ans+=4*(i-1)

        return ans
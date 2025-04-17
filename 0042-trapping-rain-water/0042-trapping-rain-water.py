class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_fill=[0]*n
        curr_max=0

        for i in range(1,n-1):
            if height[i-1] > curr_max:
                curr_max=height[i-1]
            max_fill[i]=curr_max

        curr_max=0

        for i in range(n-2,0,-1):
            if height[i+1] > curr_max:
                curr_max=height[i+1]
            max_fill[i]=min(max_fill[i], curr_max)
        
        res=0

        for i in range(1,n-1):
            fill=max_fill[i]-height[i]
            if fill>0:
                res+=fill

        return res
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0

        left=0
        right=len(height)-1

        while left < right:
            curr = (right-left) * min(height[left],height[right])
            ans = max(ans,curr)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return ans
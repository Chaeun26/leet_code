class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n=len(heights)
        ans = deque()
        curr_max = -inf

        for i in range(n-1,-1,-1):
            if curr_max < heights[i]:
                curr_max = heights[i]
                ans.appendleft(i)
        
        return list(ans)
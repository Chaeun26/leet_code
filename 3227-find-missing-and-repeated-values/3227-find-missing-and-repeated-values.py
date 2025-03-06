class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        nums={i for i in range(1,n*n+1)}
        ans=[]

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in nums:
                    ans.append(grid[i][j])
                else:
                    nums.remove(grid[i][j])

        return ans + list(nums)
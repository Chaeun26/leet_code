class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n=len(grid),len(grid[0])
        prev=None
        flatten=[]

        for i in range(m):
            for j in range(n):
                if prev==None:
                    prev=grid[i][j] % x
                if grid[i][j] % x != prev:
                    return -1
                flatten.append(grid[i][j])
        
        flatten.sort()
        med = int(m*n/2)
        med_val=flatten[med]
        ans=0
        
        for num in flatten:
            ans+=abs(num-med_val)//x
        
        return ans
        
                
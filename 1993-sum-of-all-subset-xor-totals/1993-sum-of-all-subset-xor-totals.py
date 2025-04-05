class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.n=len(nums)
        self.res=0
        
        def backtracking(idx, curr):
            if idx==self.n:
                self.res+=curr
                return 
            
            backtracking(idx+1,curr^nums[idx])
            
            backtracking(idx+1,curr)
        
        backtracking(0,0)

        return self.res

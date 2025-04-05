class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.n=len(nums)
        self.res=0
        
        def backtracking(idx, curr_subset):
            if idx==self.n:
                print(curr_subset)
                tmp=0
                for mem in curr_subset:
                   tmp ^= mem
                self.res+=tmp
                return
            
            curr_subset.append(nums[idx])
            backtracking(idx+1,curr_subset)
            curr_subset.pop()
            
            backtracking(idx+1,curr_subset)
        
        backtracking(0,[])

        return self.res

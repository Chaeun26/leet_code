class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        min_val,max_val=inf,-inf
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                min_val=min(min_val,nums[i])
        for i in range(n-2,-1,-1):
            if nums[i] > nums[i+1]:
                max_val=max(max_val,nums[i])
        
        if min_val==inf and max_val==-inf:
            return 0
        
        l=r=0
        for i in range(n):
            if min_val<nums[i]:
                l=i
                break
        for i in range(n-1,-1,-1):
            if nums[i]<max_val:
                r=i
                break

        return r-l+1
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]

        a=nums[0]
        b=max(a,nums[1])
        
        for i in range(2,n):
            tmp=b
            b=max(a+nums[i],tmp)
            a=tmp

        return b
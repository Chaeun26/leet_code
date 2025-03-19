class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]

        a1=nums[0]
        b1=max(a1,nums[1])

        for i in range(2,n-1):
            tmp=b1
            b1=max(a1+nums[i],tmp)
            a1=tmp

        a2=0 # without 1st home
        b2=max(a2,nums[1])

        for i in range(2,n):
            tmp=b2
            b2=max(a2+nums[i],tmp)
            a2=tmp

        return max(b1,b2)
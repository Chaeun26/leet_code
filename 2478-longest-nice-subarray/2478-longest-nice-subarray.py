class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans=1
        curr=j=0

        for i in range(len(nums)):
            while (nums[i] & curr) != 0 and j<len(nums):
                curr &= ~nums[j]
                j+=1
            
            curr |= nums[i]
            ans=max(ans,i-j+1)

        return ans
            
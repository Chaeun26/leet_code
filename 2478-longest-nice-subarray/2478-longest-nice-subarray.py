class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans=1
        curr=nums[0]
        j=0

        for i in range(1,len(nums)):
            while (nums[i] & curr) != 0 and j<len(nums):
                curr=curr^nums[j]
                j+=1
            
            curr=curr|nums[i]
            ans=max(ans,i-j+1)

        return ans
            
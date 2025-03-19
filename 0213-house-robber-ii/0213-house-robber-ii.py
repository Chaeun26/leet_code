class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def max_rob(nums):
            prev=ans=0

            for val in nums:
                tmp=max(ans,prev+val)
                prev=ans
                ans=tmp

            return ans
        
        return max(max_rob(nums[:-1]), max_rob(nums[1:]), nums[0])
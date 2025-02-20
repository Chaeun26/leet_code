class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=i=0
        max_sum=float('-inf')

        for j in range(len(nums)):
            if curr_sum+nums[j] < nums[j]:
                i=j
                curr_sum=nums[j]
            else:
                curr_sum+=nums[j]
            max_sum=max(max_sum, curr_sum)
        
        return max_sum

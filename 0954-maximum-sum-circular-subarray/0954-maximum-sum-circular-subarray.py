class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr=0
        max_sum=float('-inf')

        for i in range(len(nums)):
            if curr+nums[i] < nums[i]:
                curr=nums[i]
            else:
                curr+=nums[i]
            max_sum=max(max_sum,curr)

        total_sum=sum(nums[:])
        curr=0
        min_sum=float('inf')
        for i in range(len(nums)):
            if curr+nums[i] < nums[i]:
                curr+=nums[i]
            else:
                curr=nums[i]
            min_sum=min(min_sum, curr)

        if total_sum==min_sum:
            return max_sum

        return max_sum if max_sum > (total_sum-min_sum) else total_sum-min_sum
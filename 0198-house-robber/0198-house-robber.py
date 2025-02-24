class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # return max(nums[0]+self.rob(nums[2:]), self.rob(nums[1:]))

        sum = [0] * len(nums)
        sum[-1] = nums[-1]
        sum[-2] = max(nums[-1], nums[-2])

        for i in range(len(nums)-3, -1, -1):
            sum[i] = max(nums[i] + sum[i+2], sum[i+1])

        return sum[0]
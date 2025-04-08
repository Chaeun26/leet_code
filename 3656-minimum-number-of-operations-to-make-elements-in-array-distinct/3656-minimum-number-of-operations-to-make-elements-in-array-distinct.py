class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0

        while nums:
            if len(set(nums))==len(nums) or not nums:
                return cnt
            cnt+=1
            nums = nums[3:] if len(nums)>=3 else []

        if not nums:
            return cnt
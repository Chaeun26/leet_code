class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total%k!=0:
            return False
        
        nums.sort(reverse=True)
        used=[False]*len(nums)
        partial_sum = total//k
        
        def backtrack(idx, remaining, curr_sum):
            if remaining==0:
                return True

            if curr_sum==partial_sum:
                return backtrack(0,remaining-1,0)

            for i in range(idx, len(nums)):
                if used[i] or curr_sum+nums[i] > partial_sum:
                    continue
                used[i]=True
                if backtrack(i+1, remaining, curr_sum+nums[i]):
                    return True
                used[i]=False

                if curr_sum==0:
                    break

            return False

        return backtrack(0,k,0)
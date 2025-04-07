class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)
        
        def backtrack(start, k_remaining, curr_sum):
            if k_remaining == 0:
                return True
            
            if curr_sum == target:
                return backtrack(0, k_remaining - 1, 0)
            
            for i in range(start, len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i + 1, k_remaining, curr_sum + nums[i]):
                    return True
                used[i] = False
                
                # \U0001f6ab Prune: if placing nums[i] at curr_sum == 0 fails, no need to try more
                if curr_sum == 0:
                    break
            
            return False
        
        return backtrack(0, k, 0)
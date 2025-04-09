class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minimum=min(nums)

        if minimum < k:
            return -1
        
        return len(set(nums))-1 if minimum==k else len(set(nums))

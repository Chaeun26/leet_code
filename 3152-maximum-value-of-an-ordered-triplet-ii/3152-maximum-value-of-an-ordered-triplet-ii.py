class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        a=b=c=0

        for i in range(n):
            a = max(a, b*nums[i])
            b = max(b, c-nums[i])
            c = max(c, nums[i])
        
        return a
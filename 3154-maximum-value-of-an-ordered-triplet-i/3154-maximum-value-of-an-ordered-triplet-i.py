class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        curr=0

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (nums[i]-nums[j])*nums[k] > curr:
                        curr=(nums[i]-nums[j])*nums[k]
        
        return curr
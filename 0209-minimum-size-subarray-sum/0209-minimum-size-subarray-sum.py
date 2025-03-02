class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=curr=0
        ans=float('inf')
        for j in range(len(nums)):
            
            curr+=nums[j]
            
            if curr+nums[j] > target:
                while curr > target:
                    ans=min(ans,j-i+1)
                    curr-=nums[i]
                    i+=1
            
            if curr>=target:
                ans=min(ans,j-i+1)


        return ans if ans!=float('inf') else 0
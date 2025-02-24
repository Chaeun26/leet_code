class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)//2
        count=1
        nums.sort()
       
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
                if count>n:
                    return nums[i]
            else:
                count=1
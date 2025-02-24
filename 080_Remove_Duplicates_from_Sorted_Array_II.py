class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=count=1

        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count+=1
            else:
                count=1
            
            if count<=2:
                nums[k]=nums[i]
                k+=1

        return k

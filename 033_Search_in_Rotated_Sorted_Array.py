class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        
        l=0
        r=len(nums)-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l]==target:
                return l
            elif nums[r]==target:
                return r

            if nums[l] < nums[r]:
                if nums[mid]>target:
                    r-=1
                else:
                    l+=1
            elif nums[l]>=nums[r]:
                if nums[mid]>target:
                    l+=1
                else:
                    r-=1


        return -1

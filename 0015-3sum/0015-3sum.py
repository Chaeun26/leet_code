class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        nums.sort()
        
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue

            l=i+1
            r=len(nums)-1

            while l<r:
                if nums[l]+nums[r]<(-nums[i]):
                    l+=1
                elif nums[l]+nums[r]>(-nums[i]):
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l+1<len(nums) and nums[l]==nums[l+1]:
                        l+=1
                    while r-1>=0 and nums[r]==nums[r-1]:
                        r-=1
                        
                    l+=1
                    r-=1
            
        return ans
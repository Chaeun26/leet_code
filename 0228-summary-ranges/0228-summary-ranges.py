class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []

        ans=[]
        s=nums[0]

        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if s==nums[i-1]:
                    ans.append(str(s))
                else:
                    ans.append(f"{s}->{nums[i-1]}")
                s=nums[i]

        if s==nums[-1]:
            ans.append(str(s))
        else:
            ans.append(f"{s}->{nums[-1]}")
        
        return ans

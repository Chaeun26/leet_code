class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [str(nums[0])]

        ans=[]
        s=nums[0]

        for i in range(len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                e=nums[i]
                if s==e:
                    ans.append(str(s))
                else:
                    ans.append("%d->%d"%(s,e))
                s=nums[i+1]

                if i==len(nums)-2:
                    ans.append(str(s))
            else:
                if i==len(nums)-2:
                    ans.append("%d->%d"%(s,nums[i+1]))
            
        

        # for i in range(1,len(nums)):
        #     if nums[i-1]+1!=nums[i]:
        #         e=nums[i-1]
        #         if s==e:
        #             ans.append(str(s))
        #         else:
        #             ans.append("%d->%d"%(s,e))
        #         s=nums[i]

        #         if i==len(nums)-1:
        #             ans.append(str(nums[-1]))
        #     elif i==len(nums)-1:
        #         e=nums[i]
        #         ans.append("%d->%d"%(s,e))

        return ans
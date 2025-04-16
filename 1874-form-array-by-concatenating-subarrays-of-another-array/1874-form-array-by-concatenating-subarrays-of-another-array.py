class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        s=0
        e=None

        for i in range(len(nums)):
            if s<len(groups) and nums[i]==groups[s][0]:
                curr=groups[s]
                if nums[i:i+len(curr)]==curr and (e==None or e<i):
                    s+=1
                    e=i+len(curr)-1
        
        return s==len(groups)
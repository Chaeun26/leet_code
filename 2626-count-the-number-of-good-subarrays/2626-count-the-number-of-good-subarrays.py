class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        nums_cnt=defaultdict(int)
        curr_cnt=res=0
        start=0

        for i in range(len(nums)):
            curr_cnt+=nums_cnt[nums[i]]
            nums_cnt[nums[i]]+=1

            while curr_cnt>=k:
                res+=len(nums)-i
                nums_cnt[nums[start]]-=1
                curr_cnt-=nums_cnt[nums[start]]
                start+=1

        return res

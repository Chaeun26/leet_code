class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        nums_set=set(nums)
        longest=0
        for ns in nums_set:
            if ns-1 not in nums_set:
                curr=ns
                curr_len=0
                while curr in nums_set:
                    curr+=1
                    curr_len+=1
                longest=max(longest,curr_len)

        return longest
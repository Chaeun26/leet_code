class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0

        count=pos=max_pos=0

        for i in range(n-1):
            max_pos=max(max_pos, i+nums[i])

            if i==pos:
                count+=1
                pos=max_pos

        return count
            


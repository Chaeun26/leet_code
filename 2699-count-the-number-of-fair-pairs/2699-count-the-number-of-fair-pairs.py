class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        0 1 4 4 5 7

        lower - 0 = 3
        upper - 0 = 6
        find boundaries ->> 4 4 5

        1 2 5 7 9
        n=2
        curr_lower  curr_higher
        9          9
        '''
        cnt=0
        nums.sort()

        # for i,n in enumerate(nums):
        #     curr_lower=lower-n
        #     curr_upper=upper-n
            
        #     left=bisect_left(nums,curr_lower,i+1)
        #     right=bisect_right(nums, curr_upper, i+1)

        #     cnt+=right-left
        # return cnt

        return self.lower_bound(nums, upper+1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], value:int) -> int:
        left=0
        right=len(nums)-1
        cnt=0

        while left<right:
            if nums[left]+nums[right]<value:
                cnt+=right-left
                left+=1
            else:
                right-=1

        return cnt






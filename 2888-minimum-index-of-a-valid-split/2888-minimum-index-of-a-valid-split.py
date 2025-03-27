class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # split from index 0 to len(nums)-1, compare dominant between each 
        # sliding window
        n=len(nums)

        if n==1:
            return -1
        

        left=defaultdict(int)
        right=defaultdict(int)
        left_len=0
        right_len=n

        for i in range(n):
            right[nums[i]]+=1
        
        for i in range(n):
            left_len+=1
            left[nums[i]]+=1
            right_len-=1
            right[nums[i]]-=1
            
            if left[nums[i]]>left_len/2 and right[nums[i]]>right_len/2:
                return i
        
        return -1

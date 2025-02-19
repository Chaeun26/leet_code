# Solution A
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]

        l=0
        r=n-1
        minimum=float('inf')
        while l<n and r>=0 and l<=r:
            minimum=min(minimum, nums[l], nums[r])
            l+=1
            r-=1

        return minimum

# Solution B
  class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1

        while l<r:
            m=(l+r)//2

            if nums[m] > nums[r]:
                l=m+1
            else:
                r=m

        return nums[r]

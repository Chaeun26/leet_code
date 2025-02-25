class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd=0
        even=1
        curr_sum=ans=0

        for num in arr:
            curr_sum+=num

            if curr_sum%2==0:
                ans+=odd
                even+=1
            else:
                ans+=even
                odd+=1
            
        return ans % (10**9 + 7)

       

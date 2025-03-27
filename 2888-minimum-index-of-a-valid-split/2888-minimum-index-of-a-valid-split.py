class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return -1
        
        freq = Counter(nums)
        dominant = -1
        for num,count in freq.items():
            if count > n/2:
                dominant=num
                break
        
        if dominant==-1:
            return dominant
        
        left_count=0
        total_count = freq[dominant]

        for i in range(n):
            if nums[i]==dominant:
                left_count+=1
                if left_count>(i+1)/2 and total_count>(n-i+1)/2:
                    return i
                total_count-=1
        return -1
        
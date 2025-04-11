class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low, high+1):
            num=str(i)
            num_len=len(num)
            if num_len%2!=0:
                continue
            
            digits=list(map(int,num))
            half=num_len//2
            if sum(digits[:half])==sum(digits[half:]):
                cnt+=1

        return cnt
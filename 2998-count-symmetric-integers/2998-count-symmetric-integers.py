class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low, high+1):
            num=str(i)
            total=sum(map(int, num))
            num_len=len(num)

            if total%2!=0 or num_len%2!=0:
                continue

            if total//2==sum(map(int, num[:num_len//2])):
                cnt+=1

        return cnt
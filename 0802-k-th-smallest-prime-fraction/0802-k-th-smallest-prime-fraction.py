class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        low,high = 0.0,1.0
        num,den = 0,1

        while high - low > 1e-9:
            mid = (low+high)/2
            count=0
            num,den = 0,1
            j=1
            for i in range(n-1):
                while j<n and (arr[i]/arr[j])>mid:
                    j+=1
                if j==n:
                    break
                count += n-j
                if arr[i]*den > arr[j]*num:
                    num,den = arr[i],arr[j]
            if count < k:
                low=mid
            elif count > k:
                high=mid
            else:
                return [num,den]
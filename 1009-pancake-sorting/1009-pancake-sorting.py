class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        n=len(arr)

        for k in range(n,1,-1):
            max_idx=arr.index(max(arr[:k]))

            if max_idx!=0:
                ans.append(max_idx+1)
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
                # print(ans, arr)

            ans.append(k)
            arr[:k]=arr[:k][::-1]
            # print("2nd",k, arr)

        return ans
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        1 2 3 4 5
        2 1 0 1 2

        left=1 (2) -> 0 (1)
        right=2 (3) -> 3 (4) -> 4 (5)

        '''
        if len(arr)==k:
            return arr
        
        left=bisect_left(arr,x)-1
        right=left+1

        while right-left-1 < k:
            if left==-1:
                right+=1
                continue

            if right==len(arr) or abs(arr[left]-x) <= abs(arr[right]-x):
                left-=1
            else:
                right+=1

        return arr[left+1:right]
        
        # ans=[]

        # for num in arr:
        #     diff=abs(num-x)
        #     if k>0:
        #         heapq.heappush(ans,(-diff, num))
        #         k-=1
        #     else:
        #         max_diff, _=ans[0]
        #         if diff < -max_diff:
        #             heapq.heappop(ans)
        #             heapq.heappush(ans,(-diff,num))

        # ans = [val for _,val in ans]
        # ans.sort()

        # return ans
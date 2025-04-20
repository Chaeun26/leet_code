class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        1 2 3 4 5
        2 1 0 1 2

        1 2 3 4 k=4

        '''
        
        ans=[]

        for num in arr:
            diff=abs(num-x)
            if k>0:
                heapq.heappush(ans,(-diff, num))
                k-=1
            else:
                max_diff, _=ans[0]
                if diff < -max_diff:
                    heapq.heappop(ans)
                    heapq.heappush(ans,(-diff,num))

        ans = [val for _,val in ans]
        ans.sort()

        return ans
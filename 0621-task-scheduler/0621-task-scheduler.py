class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        A 0
        A 3
        A 6
        
        B 1
        B 4
        B 7

        A A B B C D
        
        2 2 1 1
        
        time=3
        q: 3,1 4,1

        A A A B B B
        time=0 1 2 3 4 5 6 7 8
        allocated = 0 4 8 1 5 9 -> 9 -> 10
        A:0->4->8
        B:1->
        '''
        count=Counter(tasks)
        max_heap=[-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        q=[]
        time=0

        while max_heap or q:
            time+=1

            if max_heap:
                freq=heapq.heappop(max_heap)+1
                if freq:
                    q.append((time+n,freq))

            if q and q[0][0]==time:
                heapq.heappush(max_heap, q.pop(0)[1])
                    
        return time
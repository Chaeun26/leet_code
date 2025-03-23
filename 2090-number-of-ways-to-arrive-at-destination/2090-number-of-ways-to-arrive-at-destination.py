class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        connections=defaultdict(list)
        min_time=[inf]*n
        ways=[0]*n
        heap=[]

        min_time[0]=0
        ways[0]=1
        heapq.heappush(heap,(0,0))

        for u,v,time in roads:
            connections[u].append((v,time))
            connections[v].append((u,time))

        
        while len(heap)>0:
            curr_time,curr_node = heapq.heappop(heap)

            if curr_time > min_time[curr_node]:
                continue
            
            for neighbor,travel_time in connections[curr_node]:
                total_time=curr_time+travel_time

                if total_time<min_time[neighbor]:
                    min_time[neighbor]=total_time
                    ways[neighbor]=ways[curr_node]
                    heapq.heappush(heap,(total_time,neighbor))
                elif total_time==min_time[neighbor]:
                    ways[neighbor]+=ways[curr_node]

        return ways[n-1] % 1000000007
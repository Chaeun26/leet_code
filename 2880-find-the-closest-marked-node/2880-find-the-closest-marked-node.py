class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph=defaultdict(list)
        distance=[inf]*n

        for u,v,w in edges:
            graph[u].append((v,w))

        start=[]
        heapq.heappush(start,(0,s))

        while start:
            dist,u=heapq.heappop(start)

            if dist > distance[u]:
                continue
            
            for v,w in graph[u]:
                if distance[v] >= dist + w:
                    distance[v] = dist + w
                    heapq.heappush(start,(distance[v],v))
        
        min_dist=inf

        for m in marked:
            min_dist=min(min_dist,distance[m])

        return min_dist if min_dist!=inf else -1
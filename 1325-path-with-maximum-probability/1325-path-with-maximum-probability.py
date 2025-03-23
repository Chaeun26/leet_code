class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        connections=defaultdict(list)
        max_prob=[0]*n
        heap=[]

        heapq.heappush(heap, (-1.0,start_node))

        for i,(u,v) in enumerate(edges):
            connections[u].append((v,succProb[i]))
            connections[v].append((u,succProb[i]))
        
        while heap:
            curr_prob,curr_node=heapq.heappop(heap)

            if -1*curr_prob < max_prob[curr_node]:
                continue
            
            for next_node,prob in connections[curr_node]:
                total_prob=curr_prob*prob*(-1)

                if total_prob > max_prob[next_node]:
                    max_prob[next_node]=total_prob
                    heapq.heappush(heap,(-1*total_prob,next_node))
            
        
        return max_prob[end_node]
        
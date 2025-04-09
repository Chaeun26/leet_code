class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = [{} for i in range(n)]
        for u,v,w in edges:
            graph[v][u]=min(graph[v].get(u,inf), w)
        
        def is_feasible(maxW):
            queue=[0]
            visited=[True] + [False]*(n-1)
            for i in queue:
                for j in graph[i]:
                    if graph[i][j] > maxW: continue
                    if visited[j]: continue
                    queue.append(j)
                    visited[j]=1
            return all(visited)

        res=bisect_left(range(10**6+1), 1, key=is_feasible)
        return res if res <= 10**6 else -1
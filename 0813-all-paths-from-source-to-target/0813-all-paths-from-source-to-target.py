class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        connections=defaultdict(list)
        n=len(graph)

        for i,neighbor in enumerate(graph):
            connections[i]=neighbor
        
        queue=deque([(0,[0])])
        ans=[]

        while queue:
            node,path=queue.popleft()

            if node==n-1:
                ans.append(path)

            for neighbor in graph[node]:
                queue.append((neighbor,path+[neighbor]))

        return ans
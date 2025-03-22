class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        visited=set()

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            start=[node]
            component=set()

            while start:
                vertex=start.pop()
                if vertex in visited:
                    continue
                visited.add(vertex)
                component.add(vertex)
                for v in graph[vertex]:
                    if v not in visited:
                        start.append(v)

            return component

        complete=0

        for i in range(n):
            if i not in visited:
                component=dfs(i)
                edges=sum(len(graph[node]) for node in component)
                k=len(component)
                if edges==k*(k-1):
                    complete+=1      

        return complete 
        

        


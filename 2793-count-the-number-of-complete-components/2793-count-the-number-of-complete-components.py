class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        self.visited=set()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node):
            start=[node]
            connected=set()

            while start:
                vertex=start.pop()
                self.visited.add(vertex)
                connected.add(vertex)

                for v in graph[vertex]:
                    if v not in self.visited:
                        start.append(v)

            return connected

        complete=0

        for i in range(n):
            if i not in self.visited:
                connected=dfs(i)
                edges=0
                for mem in connected:
                    edges+=len(graph[mem])
                k=len(connected)
                if edges//2==(k*(k-1))//2:
                    complete+=1      

        return complete 
        

        


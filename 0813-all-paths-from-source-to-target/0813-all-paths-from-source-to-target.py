class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # n=len(graph)
        
        # queue=deque([(0,[0])])
        # ans=[]

        # while queue:
        #     node,path=queue.popleft()

        #     if node==n-1:
        #         ans.append(path)

        #     for neighbor in graph[node]:
        #         queue.append((neighbor,path+[neighbor]))

        # return ans

        target=len(graph)-1
        ans=[]

        def backtracking(curr_node, path):
            if curr_node==target:
                ans.append(list(path))
                return
            
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtracking(next_node,path)
                path.pop()
            
        path=[0]
        backtracking(0,path)

        return ans
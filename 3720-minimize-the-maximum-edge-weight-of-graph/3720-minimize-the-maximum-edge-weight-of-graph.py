class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        edge_min_weight = {}
        for u, v, w in edges:
            graph[u].append((v, w))
            if (u, v) in edge_min_weight:
                edge_min_weight[(u, v)] = min(edge_min_weight[(u, v)], w)
            else:
                edge_min_weight[(u, v)] = w
        
        def is_feasible(max_weight):
            cand_graph = defaultdict(list)
            for u in range(n):
                for v, w in graph[u]:
                    if w <= max_weight:
                        cand_graph[u].append(v)
            
            rev_graph = defaultdict(list)
            for u in range(n):
                for v in cand_graph[u]:
                    rev_graph[v].append(u)
            
            visited = set()
            queue = deque([0])
            visited.add(0)
            parent = {}
            
            while queue:
                node = queue.popleft()
                for prev in rev_graph[node]:
                    if prev not in visited:
                        visited.add(prev)
                        queue.append(prev)
                        parent[prev] = node
            
            if len(visited) != n:
                return False
            
            out_degree = defaultdict(int)
            max_used_weight = 0
            for child, par in parent.items():
                out_degree[child] += 1
                if out_degree[child] > threshold:
                    return False
                weight = edge_min_weight[(child, par)]
                max_used_weight = max(max_used_weight, weight)
            
            return max_used_weight <= max_weight
        
        weights = sorted(set(w for _,_,w in edges))
        left,right=0,len(weights)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            max_weight=weights[mid]
            
            if is_feasible(max_weight):
                ans=max_weight
                right=mid-1
            else:
                left=mid+1
        return ans
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        visited={}
        new_root = {}
        def dfs(var, group_num):
            stack = [(var, 1.0)]
            while stack:
                curr_var, curr_value = stack.pop()
                if curr_var not in visited:
                    visited[curr_var] = (curr_value, group_num)
                    for i in range(len(equations)):
                        if curr_var == equations[i][0] and equations[i][1] not in visited:
                            stack.append((equations[i][1], curr_value / values[i]))
                        elif curr_var == equations[i][1] and equations[i][0] not in visited:
                            stack.append((equations[i][0], curr_value * values[i]))

        
        for i in range(len(values)):
            if equations[i][0] not in visited:
                dfs(equations[i][0], i)
                    
        ans = [-1.0]*len(queries)
        for i in range(len(queries)):
            if queries[i][0] in visited and queries[i][1] in visited:
                var0, group_num_0 = visited.get(queries[i][0],[])
                var1, group_num_1 = visited.get(queries[i][1],[])
            
                if group_num_0==group_num_1:
                    ans[i]=var0/var1
        return ans

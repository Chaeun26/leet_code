class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific=set()
        atlantic=set()

        def bfs(r,c):
            queue=deque([(r,c)])
            visited=set()
            visited.add((r,c))
            while queue:
                x,y=queue.popleft()
                for dx,dy in {(0,1),(0,-1),(1,0),(-1,0)}:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and heights[x][y]<=heights[nx][ny]:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            return visited

        for c in range(n):
            pacific|=bfs(0,c)
        for r in range(m):
            pacific|=bfs(r,0)

        for c in range(n):
            atlantic|=bfs(m-1,c)
        for r in range(m):
            atlantic|=bfs(r,n-1)

        return list(pacific & atlantic)


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1

        n=len(grid)
        visited=set()
        directions=[(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]

        q=deque([(0,0,1)])
        visited.add((0,0))

        while q:
            x,y,cnt=q.popleft()

            if x==n-1 and y==n-1:
                return cnt

            for dx,dy in directions:
                nx=x+dx
                ny=y+dy
                if 0<=nx<n and 0<=ny<n and ((nx,ny) not in visited) and grid[nx][ny]==0:
                    q.append((nx,ny,cnt+1))
                    visited.add((nx,ny))

        return -1

    '''
    1 0 0
    1 1 0
    1 1 0

    '''
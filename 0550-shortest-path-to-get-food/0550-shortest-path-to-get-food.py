from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])

        q=deque()
        visited=set()

        for r in range(m):
            for c in range(n):
                if grid[r][c]=="*":
                    q.append((r,c,0))
                    visited.add((r,c))
                    break
        
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        while q:
            x,y,count= q.popleft()

            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    if grid[nx][ny]=="O":
                        visited.add((nx,ny))
                        q.append((nx,ny,count+1))
                    elif grid[nx][ny]=="#":
                        return count+1

        return -1
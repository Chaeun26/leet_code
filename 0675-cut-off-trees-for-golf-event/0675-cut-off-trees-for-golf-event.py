from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m,n=len(forest),len(forest[0])
                
        trees = sorted([(forest[x][y],x,y) for x in range(m) for y in range(n) if forest[x][y] > 1])
        
        def bfs(x,y,targetX,targetY):
            q=deque([(x,y,0)])
            visited=set()
            visited.add((x,y))
            
            while q:
                x,y,step=q.popleft()
                
                if x==targetX and y==targetY:
                    return step
                
                for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n:
                        if (nx,ny) not in visited and forest[nx][ny]!=0:
                            q.append((nx,ny,step+1))
                            visited.add((nx,ny))
                            
            return -1
        
        total=0
        startX,startY=0,0
        
        for _,x,y in trees:
            step=bfs(startX,startY,x,y)
            if step==-1:
                return -1
            total+=step
            startX,startY=x,y
            
            
        return total
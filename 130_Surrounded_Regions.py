from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])

        def bfs(r,c):
            queue=deque([(r,c)])
            board[r][c]='T'
            while queue:
                x,y=queue.popleft()
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                        board[nx][ny]='T'
                        queue.append((nx,ny))

        for r in range(m):
            for c in range(n):
                if r==0 or r==m-1 or c==0 or c==n-1:
                    if board[r][c]=='O':
                        bfs(r,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'

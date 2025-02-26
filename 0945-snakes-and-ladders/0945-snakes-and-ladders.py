from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def get_position(num):
            r = (n-1) - (num-1) // n
            c = (num - 1) % n
            if (n-1-r)%2 == 1:
                c = (n-1) - c
            return r,c

        n = len(board)
        queue = deque([(1,0)])
        visited = set([1])

        while queue:
            curr,count = queue.popleft()

            if curr==n*n:
                return count
            
            for i in range(1,7):
                next_pos = curr + i
                if next_pos > n*n:
                    continue

                r,c = get_position(next_pos)

                if board[r][c]!=-1:
                    next_pos = board[r][c]
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos,count+1))

        return -1
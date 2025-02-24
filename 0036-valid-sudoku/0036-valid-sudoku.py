class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    if ("r", r, board[r][c]) not in seen:
                        seen.add(("r", r,board[r][c]))
                    else:
                        return False
                    
                    if ("c", c, board[r][c]) not in seen:
                        seen.add(("c", c,board[r][c]))
                    else:
                        return False
                    
                    sec = (r//3,c//3)
                    if ("s", sec, board[r][c]) not in seen:
                        seen.add(("s",sec,board[r][c]))
                    else:
                        return False
            
        return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr=[["."]*n for _ in range(n)]
        result=[]

        def backtracking(r,cols,main_diag,anti_diag):
            if r==n:
                result.append(["".join(row) for row in curr])
                return
                      
            for c in range(n):
                if c in cols or r-c in main_diag or r+c in anti_diag:
                    continue
                
                cols.add(c)
                main_diag.add(r-c)
                anti_diag.add(r+c)

                curr[r][c]="Q"

                backtracking(r+1,cols,main_diag,anti_diag)

                cols.remove(c)
                main_diag.remove(r-c)
                anti_diag.remove(r+c)
                curr[r][c]="."

            return

        backtracking(0,set(),set(),set())
        return result
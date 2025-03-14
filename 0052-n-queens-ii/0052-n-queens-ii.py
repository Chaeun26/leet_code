class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r,cols,main_diag,anti_diag):
            if r==n:
                return 1
            
            count=0
            for c in range(n):
                if c in cols or (r-c) in main_diag or (r+c) in anti_diag:
                    continue
                
                cols.add(c)
                main_diag.add(r-c)
                anti_diag.add(r+c)

                count+=backtrack(r+1,cols,main_diag,anti_diag)

                cols.remove(c)
                main_diag.remove(r-c)
                anti_diag.remove(r+c)

            return count

        return backtrack(0,set(),set(),set())
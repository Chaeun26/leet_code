class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]

        def backtrack(open,close,curr_pair):
            if open==n and close==n:
                ans.append(curr_pair)
                return

            if open<n:
                backtrack(open+1,close,curr_pair+"(")
            if open>0 and open>close:
                backtrack(open,close+1,curr_pair+")")

        backtrack(0,0,"")

        return ans
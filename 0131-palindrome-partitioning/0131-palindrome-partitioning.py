class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def isPalindrome(subs):
            return subs==subs[::-1]

        def backtrack(idx,ans):
            if idx==len(s):
                res.append(ans[:])
                return

            for i in range(idx+1, len(s)+1):
                subs = s[idx:i]
                if isPalindrome(subs):
                    ans.append(subs)
                    backtrack(i, ans)
                    ans.pop()

        backtrack(0,[])

        return res
        
        '''
        idx = 0 -> "a" backtrack(1,"a", []) -> backtrack(2,"aa",[]) -> ans = ["aa"] backtrack(3,"b",["aa"]) =>> [["aa","b"]]
                                                backtrack(2, "a", ["a"]) -> backtrack(3,"b", ["a","a"]) =>> [["aa","b"], ["a","a","b"]]

        '''
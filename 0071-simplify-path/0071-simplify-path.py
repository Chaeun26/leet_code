from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs=path.split("/")
        ans=[]
        
        for c in dirs:
            if c=="..":
                if ans:
                    ans.pop()
            elif c and c!=".":
                ans.append(c)

        return "/" + "/".join(ans)
class Solution:
    def partitionString(self, s: str) -> int:
        cnt=0
        prev=set()
        n=len(s)
        for i in range(n):
            if s[i] in prev:
                prev.clear()
                prev.add(s[i])
                cnt+=1
            else:
                prev.add(s[i])

        return cnt+1 if prev else cnt
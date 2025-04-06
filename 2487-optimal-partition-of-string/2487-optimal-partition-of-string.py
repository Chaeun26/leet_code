class Solution:
    def partitionString(self, s: str) -> int:
        cnt=1
        last_idx = [-1]*26
        start=0
        n=len(s)
        for i in range(n):
            if last_idx[ord(s[i])-ord('a')] >= start:
                cnt+=1
                start=i
            last_idx[ord(s[i])-ord('a')]=i

        return cnt
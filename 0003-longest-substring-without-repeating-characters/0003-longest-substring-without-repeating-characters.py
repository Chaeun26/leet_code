class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        prev=set()
        ans=l=0

        for i,c in enumerate(s):
            if c not in prev:
                prev.add(c)
            else:
                ans=max(ans,i-l)
                
                while c in prev:
                    prev.remove(s[l])
                    l+=1
                
                prev.add(c)

        ans=max(ans,i-l+1)
        return ans
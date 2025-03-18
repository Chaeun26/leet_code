class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        j=count=0
        tmp=set()

        for i in range(len(s)):
      
            while s[i] in tmp or len(tmp)>=k:
                tmp.remove(s[j])
                j+=1

            if s[i] not in tmp:
                tmp.add(s[i])

            if len(tmp)==k:
                count+=1
                

        return count
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count=0
        
        for i in range(len(s)-k+1):
            tmp=set(s[i:i+k])
            if len(tmp)==k:
                count+=1

        return count
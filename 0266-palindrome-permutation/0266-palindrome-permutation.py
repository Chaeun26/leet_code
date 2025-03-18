class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mapping={}
        odd=0

        for c in s:
            if c not in mapping:
                mapping[c]=1
            else:
                mapping[c]+=1

        for key in mapping:
            if mapping[key]%2!=0:
                odd+=1
                
        return True if odd<=1 else False
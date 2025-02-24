class Solution:
    def romanToInt(self, s: str) -> int:

        ans=0
        for i, c in enumerate(s):
            if c=='I':
                ans+=1
            elif c=='V':
                if i-1 >= 0 and s[i-1]=='I':
                    ans+=3
                else:
                    ans+=5
            elif c=='X':
                if i-1 >= 0 and s[i-1]=='I':
                    ans+=8
                else:
                    ans+=10
            elif c=='L':
                if i-1 >= 0 and s[i-1]=='X':
                    ans+=30
                else:
                    ans+=50
            elif c=='C':
                if i-1 >= 0 and s[i-1]=='X':
                    ans+=80
                else:
                    ans+=100
            elif c=='D':
                if i-1 >= 0 and s[i-1]=='C':
                    
                    ans+=300
                else:
                    ans+=500
            elif c=='M':
                if i-1 >= 0 and s[i-1]=='C':
                    ans+=800
                else:
                    ans+=1000
                
        return ans
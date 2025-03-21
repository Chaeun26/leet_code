class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        string=""
        stack=[]

        for c in s:
            if c.isdigit():
                num=num*10+int(c)
            elif c=="[":
                stack.append((string,num))
                num=0
                string=""
            elif c=="]":
                string2,val=stack.pop()
                string=string2+val*string
            else:
                string+=c
        
        return string
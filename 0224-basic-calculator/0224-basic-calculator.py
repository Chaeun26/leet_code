class Solution:
    def calculate(self, s: str) -> int:
        curr=num=0
        operator=""
        sign=1
        stack=[]

        for c in s:
            if c=="(":
                stack.append((curr,sign))
                curr=0
                sign=1
            elif c==")":
                curr+=sign*num
                prev,prev_sign=stack.pop()
                curr=prev + prev_sign*curr
                num=0
            elif c.isdigit():
                num=num*10+int(c)
            elif c in "+-":
                curr += sign*num
                sign=1 if c=="+" else -1
                num=0

        curr+=sign*num
        return curr
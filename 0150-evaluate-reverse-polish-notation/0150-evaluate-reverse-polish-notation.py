class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])

        operands = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: x/y
        }
        stack=[]
        ans=float('inf')
        for t in tokens:
            if t=="+" or t=="-" or t=="/" or t=="*":
                a=int(stack.pop())
                b=int(stack.pop())

                stack.append(int(operands[t](b,a)))
            else:
                stack.append(t)
        
        return stack[0]
class Solution:
    def calculate(self, s: str) -> int:
        hier={"+":1,"-":1,"*":2,"/":2,"(":3,")":3}

        def cal(num_stack,op_stack):
            operator=op_stack.pop()
            num2=num_stack.pop()
            num1=num_stack.pop()
            if operator=="+":
                num_stack.append(num1+num2)
            elif operator=="-":
                num_stack.append(num1-num2)
            elif operator=="*":
                num_stack.append(num1*num2)
            elif operator=="/":
                num_stack.append(int(num1/num2))
            return

        num=0
        has_num = False
        num_stack=[]
        op_stack=[]
        for c in s:
            if c==" ":
                continue
            elif c.isdigit():
                num=num*10+int(c)
                has_num=True
            elif c=="(":
                op_stack.append(c)
            elif c==")":
                if has_num:
                    num_stack.append(num)
                    num=0
                    has_num=False
                while op_stack[-1]!="(":
                    cal(num_stack,op_stack)
                op_stack.pop()
            else:
                curr_op=c
                if has_num:
                    num_stack.append(num)
                    num=0
                    has_num=False
                while op_stack and op_stack[-1]!="(" and hier[op_stack[-1]]>=hier[curr_op]:
                    cal(num_stack,op_stack)

                op_stack.append(curr_op)
        
        if has_num:
            num_stack.append(num)

        while op_stack:
            cal(num_stack,op_stack)

        return num_stack[-1]
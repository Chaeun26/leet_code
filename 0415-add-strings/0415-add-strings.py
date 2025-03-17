class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=[]

        carry=0
        i,j=len(num1)-1,len(num2)-1

        while i>=0 or j>=0:
            a=ord(num1[i])-ord('0') if i>=0 else 0
            b=ord(num2[j])-ord('0') if j>=0 else 0
            val=(a+b+carry)%10
            carry=(a+b+carry)//10
            ans.append(val)
            i-=1
            j-=1
        
        if carry:
            ans.append(carry)

        return ''.join(str(x) for x in ans[::-1])
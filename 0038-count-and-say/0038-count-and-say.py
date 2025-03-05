class Solution:
    def countAndSay(self, n: int) -> str:
        # if n==1:
        #     return "1"
#         else:
#             s=self.countAndSay(n-1)
            
#             prev=s[0]
#             count=1
#             ans=""
#             for i in range(1,len(s)):
#                 if s[i]==prev:
#                     count+=1
#                 else:
#                     ans += str(count) + prev
                    
#                     prev=s[i]
#                     count=1

#             ans += str(count) + s[-1]
                
#             return ans
        
        k=1
        s="1"
        
        while k<n:
            prev=s[0]
            count=1
            ans=""
            for i in range(1,len(s)):
                if s[i]==prev:
                    count+=1
                else:
                    ans += str(count) + prev
                    
                    prev=s[i]
                    count=1

            ans += str(count) + s[-1]
            s=ans
            k+=1
        
        return s
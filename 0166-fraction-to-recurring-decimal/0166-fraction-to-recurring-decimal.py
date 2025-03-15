class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        
        ans="-" if (numerator < 0) ^ (denominator<0) else ""
        
        numerator=abs(numerator)
        denominator=abs(denominator)
        
        ans+=str(numerator//denominator)
        
        rem = numerator%denominator
                
        if rem==0:
            return ans
        
        ans+="."
        mp={}
        
        while rem>0:
            if rem in mp:
                ans=ans[:mp[rem]]+"(" + ans[mp[rem]:] + ")"
                break
                
            mp[rem]=len(ans)
            
            rem=rem*10
            
            ans+=str(rem//denominator)
            rem=rem%denominator
        
        return ans
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+carry < 10:
                digits[i] += 1
                return digits
            else:
                carry=1
                digits[i] = 0
                
        if carry==1:
            if digits[0]==0:
                return [1] + digits
            else:
                digits[0]+=1
                return digits

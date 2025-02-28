class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True

        original_x=x
        reverse_x=0
        while x>0:
            tmp = x%10
            x = x//10

            reverse_x*=10
            reverse_x+=tmp

        return True if original_x==reverse_x else False
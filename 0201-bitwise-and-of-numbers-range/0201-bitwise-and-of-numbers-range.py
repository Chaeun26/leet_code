class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # count=0
        # while left!=right:
        #     left=left>>1
        #     right=right>>1
        #     count+=1
        
        # for i in range(count):
        #     left=left<<1
    
        # return left

        while left < right:
            right = right & (right-1)
        return right
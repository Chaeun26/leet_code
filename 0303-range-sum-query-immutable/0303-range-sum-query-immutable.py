class NumArray:

    def __init__(self, nums: List[int]):
        self.sums=[]

        for i,j in enumerate(nums):
            if i>0:
                self.sums.append(j+self.sums[i-1])
            else:
                self.sums.append(j)   

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.sums[right]-self.sums[left-1]
        
        return self.sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
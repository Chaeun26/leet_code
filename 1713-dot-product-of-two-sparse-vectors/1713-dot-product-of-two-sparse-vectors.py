class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros={i:n for i,n in enumerate(nums) if n!=0}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.non_zeros[i]*vec.non_zeros[i] for i in self.non_zeros if i in vec.non_zeros)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
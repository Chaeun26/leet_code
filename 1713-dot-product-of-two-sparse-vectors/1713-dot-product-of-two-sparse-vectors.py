class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros=defaultdict(int)
        for i,n in enumerate(nums):
            if n!=0:
                self.non_zeros[i]=n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans=0
        v1_key_set=set(self.non_zeros.keys())
        v2_key_set=set(vec.non_zeros.keys())
        common_key=v1_key_set & v2_key_set
        
        for key in common_key:
            ans+=self.non_zeros[key]*vec.non_zeros[key]

        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
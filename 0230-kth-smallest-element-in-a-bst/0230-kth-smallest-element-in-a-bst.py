# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank=0
        def in_order(node):
            if node==None:
                return
            
            left=in_order(node.left)
            if left!=None:
                return left
            self.rank+=1
            if self.rank==k:
                return node.val
            
            return in_order(node.right)

        return in_order(root)
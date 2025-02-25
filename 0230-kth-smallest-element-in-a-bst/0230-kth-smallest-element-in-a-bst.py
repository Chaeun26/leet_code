# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank=0
        self.ans=None
        def in_order(node):
            if node==None:
                return
            
            in_order(node.left)
            self.rank+=1
            if self.rank==k:
                self.ans=node.val
            in_order(node.right)


        in_order(root)

        return self.ans
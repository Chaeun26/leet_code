# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev=None
        self.ans=True
        def in_order(node):
            if node==None:
                return

            in_order(node.left)
            if self.prev!=None:
                if self.prev >= node.val:
                    self.ans=False
            self.prev=node.val
            
            in_order(node.right)

        in_order(root)
        return self.ans

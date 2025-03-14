# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans=float('inf')
        self.prev=None

        def in_order(node):
            if not node:
                return
            
            in_order(node.left)
            if self.prev!=None:
                self.ans=min(self.ans,abs(self.prev-node.val))
            self.prev=node.val
            in_order(node.right)

        in_order(root)
        return self.ans

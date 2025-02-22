# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inversion(node):
            if node==None:
                return

            inversion(node.left)
            inversion(node.right)

            tmp=node.right
            node.right=node.left
            node.left=tmp

            return 

        inversion(root)
        return root

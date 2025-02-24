# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if root is None:
            return 0
        elif root.left and root.right:
            # depth += 1
            depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        elif root.left:
            # depth += 1
            depth += self.maxDepth(root.left)
        elif root.right:
            # depth += 1
            depth += self.maxDepth(root.right)

        return depth
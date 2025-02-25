# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0

        stack=[root]

        while stack:
            node=stack.pop()

            if node:
                count+=1
                stack.append(node.left)
                stack.append(node.right)

        return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        
        stack=[(root,0)]

        while stack:
            node,curr=stack.pop()

            if node:
                curr+=node.val

                if curr==targetSum and node.left==None and node.right==None:
                    return True

                stack.append((node.left, curr))
                stack.append((node.right, curr))

        return False

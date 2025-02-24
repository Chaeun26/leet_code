# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        stack=[(root,0)]

        while(stack):
            node,curr=stack.pop()

            if node:
                curr = curr*10 + node.val
                if node.left==None and node.right==None:
                    ans += curr

                stack.append((node.left, curr))
                stack.append((node.right, curr))

        return ans

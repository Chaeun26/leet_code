# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def dfs(node):
            if not node:
                return (0,0)

            increasing_left,decreasing_left=dfs(node.left)
            increasing_right,decreasing_right=dfs(node.right)

            increasing=decreasing=1

            if node.left:
                if node.left.val==node.val+1:
                    increasing=increasing_left+1
                elif node.val==node.left.val+1:
                    decreasing=decreasing_left+1

            if node.right:
                if node.right.val==node.val+1:
                    increasing=max(increasing,increasing_right+1)
                elif node.val==node.right.val+1:
                    decreasing=max(decreasing,decreasing_right+1)
            
            self.ans=max(self.ans,increasing+decreasing-1)

            return (increasing,decreasing)
        
        dfs(root)
        return self.ans
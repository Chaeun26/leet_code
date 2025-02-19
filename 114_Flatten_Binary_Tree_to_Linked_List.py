# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost=rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

        # Prev Solution ...   
        # def pre_order(node,isRoot):
        #     nonlocal root
        #     if not node:
        #         return
            
        #     tmpl=tmpr=None
        #     if node.left:
        #         tmpl = node.left
        #     if node.right:
        #         tmpr = node.right

        #     if not isRoot:
        #         root.right = TreeNode(node.val)
        #         root.left = None
        #         root = root.right
        #     else:
        #         root.left = None

        #     pre_order(tmpl, False)
        #     pre_order(tmpr, False)

        # pre_order(root,True)

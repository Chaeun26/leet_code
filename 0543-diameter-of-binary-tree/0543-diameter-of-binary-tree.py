# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''

        leaf node with level?
        different parent & deepest level

                1
            2            3
        
        4       5
            6       7
        '''
        diameter=[0]

        def post_traverse(node):
            if not node:
                return 0
            
            left_depth=post_traverse(node.left)
            right_depth=post_traverse(node.right)

            diameter[0]=max(diameter[0],left_depth+right_depth)

            return 1 + max(left_depth,right_depth)

        post_traverse(root)

        return diameter[0]
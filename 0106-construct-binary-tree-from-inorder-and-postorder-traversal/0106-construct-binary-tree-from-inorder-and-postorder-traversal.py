# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx = {node:idx for idx,node in enumerate(inorder)}
        post_idx=[len(postorder)-1]

        def build_tree(maps,postorder,idx,left,right):
            if left>right:
                return

            val = postorder[idx[0]]
            idx[0]-=1

            root = TreeNode(val)
            idx2 = maps[val]

            root.right = build_tree(maps,postorder,idx,idx2+1,right)
            root.left = build_tree(maps,postorder,idx,left,idx2-1)

            return root

        return build_tree(inorder_idx,postorder,post_idx,0,len(postorder)-1)

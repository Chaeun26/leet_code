# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idx=[0]
        inorder_index={value:idx for idx,value in enumerate(inorder)}

        def build_tree(inorder_index,idx,left,right):
            if left>right:
                return
            
            root=TreeNode(preorder[idx[0]])
            idx[0]+=1

            idx2=inorder_index[root.val]

            root.left = build_tree(inorder_index,idx,left,idx2-1)
            root.right = build_tree(inorder_index,idx,idx2+1,right)

            return root

        return build_tree(inorder_index,idx,0,len(inorder)-1)
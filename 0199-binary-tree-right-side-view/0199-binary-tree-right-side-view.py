# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        queue=[root]

        while queue:
            q_len = len(queue)

            for i in range(q_len):
                node = queue.pop(0)
                
                if i==q_len-1:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans

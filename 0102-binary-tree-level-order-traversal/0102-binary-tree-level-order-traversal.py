# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue=[root]
        ans=[]
        while queue:
            q_len=len(queue)
            tmp=[]
            for i in range(q_len):
                node=queue.pop(0) 

                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(tmp)>0:
                ans.append(tmp)

        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        queue=deque([(root,0)])
        
        while queue:
            qlen=len(queue)
            _,s = queue[0]
            _,e = queue[-1]
            ans=max(ans, e-s+1)

            for i in range(qlen):
            
                node, idx = queue.popleft()
                
                if node.left:
                    queue.append((node.left,2*idx))
                if node.right:
                    queue.append((node.right,2*idx+1))

                
        return ans
        
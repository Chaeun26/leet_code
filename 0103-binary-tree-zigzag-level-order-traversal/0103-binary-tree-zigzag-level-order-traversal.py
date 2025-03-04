# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        ans=[]
        direct=1
        while queue:
            qlen=len(queue)
            nodes=[]
            for i in range(qlen):
                node=queue.popleft()

                if node:
                    if direct==1:
                        nodes.append(node.val)
                    else:
                        nodes.insert(0,node.val)

                    queue.append(node.left)
                    queue.append(node.right)
            direct=direct*-1
            if nodes:
                ans.append(nodes)

        return ans
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue=deque([(p,q)])

        while queue:
            nodeP, nodeQ = queue.popleft()

            if nodeP and nodeQ:
                if nodeP.val!=nodeQ.val:
                    return False

                queue.append((nodeP.left,nodeQ.left))
                queue.append((nodeP.right,nodeQ.right))
            elif nodeP or nodeQ:
                return False

        return True
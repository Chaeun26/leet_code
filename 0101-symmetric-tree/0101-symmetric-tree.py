# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        preq = deque([root])
        postq = deque([root])

        while preq or postq:
            qlen=len(preq)

            for _ in range(qlen):
                pre = preq.popleft()
                post = postq.popleft()

                if pre and post:
                    if pre.val!=post.val:
                        return False

                    preq.append(pre.left)
                    preq.append(pre.right)

                    postq.append(post.right)
                    postq.append(post.left)
                elif pre or post:
                    return False
        
        if preq or postq:
            return False

        return True
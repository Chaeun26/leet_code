"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents=set()
        parents.add(p.val)
        parents.add(q.val)

        while p or q:
            if p and p.parent:
                if p.parent.val in parents:
                    return p.parent
                parents.add(p.parent.val)
                p=p.parent
            if q and q.parent:
                if q.parent.val in parents:
                    return q.parent
                parents.add(q.parent.val)
                q=q.parent

#         '''
#                 1
#             2            3
#                 4           
#         '''

# class Solution:
#     def get_depth(self,node:'Node') -> int:
#         depth=0
#         while node:
#             node=node.parent
#             depth+=1
#         return depth
#     def lowestCommonAncestor(self, p:'Node', q:'Node') -> 'Node':
#         p_depth=self.get_depth(p)
#         q_depth=self.get_depth(q)

#         for i in range(p_depth-q_depth):
#             p=p.parent
#         for i in range(q_depth-p_depth):
#             q=q.parent
        
#         while p!=q:
#             p=p.parent
#             q=q.parent
        
#         return p

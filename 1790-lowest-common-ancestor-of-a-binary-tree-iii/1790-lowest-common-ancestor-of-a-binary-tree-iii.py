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

        '''
                1
            2            3
                4           
        '''

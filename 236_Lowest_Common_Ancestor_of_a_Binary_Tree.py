# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents={}
        p_parent=[]
        q_parent=[]

        stack=[[root,None]]
        while stack:
            node,parent=stack.pop()

            if node:
                ancestor=parent

                if node==p:
                    p_parent.append(p)
                    while ancestor:
                        p_parent.append(ancestor)
                        ancestor=parents[ancestor]
                if node==q:
                    q_parent.append(q)
                    while ancestor:
                        q_parent.append(ancestor)
                        ancestor=parents[ancestor]
                
                parents[node]=parent

                stack.append([node.left,node])
                stack.append([node.right,node])
        if len(p_parent)==0:
            return p
        elif len(q_parent)==0:
            return q
        
        for pp in p_parent:
            for qq in q_parent:
                if pp==qq:
                    return pp

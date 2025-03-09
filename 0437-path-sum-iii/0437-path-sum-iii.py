# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count=0
        stack=[(root, [])]
        
        while stack:
            node,sums=stack.pop()
            
            if node:
                tmp=[]
                tmp.append(node.val)
                for s in sums:
                    tmp.append(s+node.val)

                    if s+node.val==targetSum:
                        print(node.val)
                        count+=1
                if node.val==targetSum:
                    count+=1
                
                stack.append((node.left,tmp))
                stack.append((node.right,tmp))
                
        return count
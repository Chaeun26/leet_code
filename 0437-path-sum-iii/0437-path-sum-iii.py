# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # count=0
        # stack=[(root, [])]
        
        # while stack:
        #     node,sums=stack.pop()
            
        #     if node:
        #         tmp=[]
        #         tmp.append(node.val)
        #         for s in sums:
        #             tmp.append(s+node.val)

        #             if s+node.val==targetSum:
        #                 print(node.val)
        #                 count+=1
        #         if node.val==targetSum:
        #             count+=1
                
        #         stack.append((node.left,tmp))
        #         stack.append((node.right,tmp))
                
        # return count
        count=0
        def preorder(node,curr_sum):
            nonlocal count
            if not node:
                return
            
            curr_sum+=node.val

            if curr_sum==targetSum:
                count+=1
            
            count+=h[curr_sum-targetSum]

            h[curr_sum]+=1

            preorder(node.left,curr_sum)
            preorder(node.right,curr_sum)

            h[curr_sum]-=1
        
        h=defaultdict(int)
        preorder(root,0)
        return count
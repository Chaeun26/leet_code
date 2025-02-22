# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue=[root]
        ans=[]

        while queue:
            num_of_nodes=len(queue)
            tmp=0
            for i in range(num_of_nodes):
                node = queue.pop(0)
                if node:
                    tmp+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(tmp/num_of_nodes)

        return ans

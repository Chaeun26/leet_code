"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        leftmost=root

        while leftmost:
            head=leftmost
            while head:
                if head.left:
                    head.left.next=head.right
                if head.right and head.next:
                    head.right.next=head.next.left
                head=head.next
            leftmost=leftmost.left
        
        return root

        # q=deque([root])

        # while q:
        #     q_len=len(q)

        #     for i in range(q_len-1):
        #         node=q.popleft()
        #         node.next=q[0]
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     node=q.popleft()
        #     node.next=None
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return root

        # time complexity O(N)
        # space complexity O(N)

        
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False

        prev=head
        curr=head.next

        while prev!=curr:
            if curr==None or curr.next==None:
                return False
            prev=prev.next
            curr=curr.next.next
        return True

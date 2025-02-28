# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        n,tmp = 1,head

        while tmp.next:
            tmp = tmp.next
            n+=1

        k=k%n
        if k==0:
            return head

        slow=head
        for _ in range(n-k-1):
            slow=slow.next
        
        new_head=slow.next
        slow.next=None
        tmp.next = head

        return new_head
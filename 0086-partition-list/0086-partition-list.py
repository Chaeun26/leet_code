# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        tmp = head
        small_dummy=ListNode(0)
        large_dummy=ListNode(0)

        tmp=head
        tmp1=small_dummy
        tmp2=large_dummy

        while tmp:
            if tmp.val >= x:
                tmp2.next=tmp
                tmp2 = tmp2.next
            else:
                tmp1.next=tmp
                tmp1 = tmp1.next
            tmp = tmp.next

        tmp2.next=None
        tmp1.next=large_dummy.next

        return small_dummy.next
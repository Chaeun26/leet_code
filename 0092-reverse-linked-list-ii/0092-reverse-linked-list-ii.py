# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        count=0
        dummy = ListNode(0)
        dummy.next=head
        pointer=dummy
        while pointer:
            count+=1
            if count==left:
                prev=pointer
                start = prev.next
                then = start.next

                for _ in range(right - left):
                    tmp = then.next
                    then.next=prev.next
                    prev.next=then
                    then = tmp
                    start.next = tmp

                return dummy.next

            
            pointer = pointer.next

        return head
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0

        while curr:
            count+=1
            curr=curr.next

        if n==count:
            return head.next

        i=1
        curr=head
        while i<count-n:
            curr=curr.next
            i+=1
            print(curr.val)
        

        if curr.next==None:
            head=None
        else:
            curr.next=curr.next.next

        return head

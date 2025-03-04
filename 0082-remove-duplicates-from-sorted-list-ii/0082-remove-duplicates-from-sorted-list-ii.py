# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy

        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                
                prev.next=head.next
            else:
                prev=prev.next
            
            head=head.next

        return dummy.next

        # if head==None or head.next==None:
        #     return head

        # dummy=ListNode(-101)
        # pointer2=dummy
        # pointer=head
        # prev=None
        # count=idx=0
        # while pointer:
        #     if prev==None:
        #         prev=pointer
        #         count=1
        #     elif prev.val!=pointer.val:
        #         if count==1:
        #             pointer2.next=ListNode(prev.val)
        #             pointer2=pointer2.next

        #         if pointer.next==None:
        #             pointer2.next=ListNode(pointer.val)
        #         count=1
        #         prev=pointer
        #     else:
        #         count+=1
        #     pointer = pointer.next
        #     idx+=1

        # return dummy.next

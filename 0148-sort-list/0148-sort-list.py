# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def find_mid(ll):
            slow,fast=ll,ll.next

            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

            return slow

        def merge(l1,l2):
            dummy=ListNode(0)
            tail=dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 or l2
            return dummy.next
        
        def merge_sort(ll):
            if ll==None or ll.next==None:
                return ll
            
            mid = find_mid(ll)
            right_head = mid.next
            mid.next = None

            left = merge_sort(ll)
            right = merge_sort(right_head)

            return merge(left,right)

        return merge_sort(head)
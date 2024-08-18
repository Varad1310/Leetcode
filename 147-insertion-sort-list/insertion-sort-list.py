# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=head
        while current!=None:
            prev=dummy
            nextnode=current.next
            while prev.next!=None and prev.next.val<current.val:
                prev=prev.next
            current.next=prev.next
            prev.next=current
            current=nextnode
        return dummy.next
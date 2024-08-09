# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            Newnode=current.next
            current.next=prev
            prev=current
            current=Newnode
        firsthalf=head
        secondhalf=prev
        while secondhalf:
            if firsthalf.val !=secondhalf.val:
                return False
            firsthalf=firsthalf.next
            secondhalf=secondhalf.next
        return True
        
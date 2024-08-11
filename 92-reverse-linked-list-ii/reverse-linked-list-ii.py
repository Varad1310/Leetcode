# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left==right:
            return head
        current=ListNode(0,head)
        prev=current
        for i in range(left-1):
            prev=prev.next
        newnode=prev.next
        for i in range(right-left):
            temp=newnode.next
            newnode.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return current.next
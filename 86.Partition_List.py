# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head = ListNode(0)
        great_head = ListNode(0)
        less, great = less_head, great_head
        curr = head
        while curr:
            nxt = curr.next
            if curr.val < x:
                less.next = curr
                less = less.next
                curr.next = None
            else:
                great.next = curr
                great = great.next
                curr.next = None
            curr = nxt
        if less:
            less.next = great_head.next
            return less_head.next
        else:
            return great_head.next

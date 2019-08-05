# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        leftover = 0

        c1, c2 = l1, l2
        dummy = cur = ListNode(0)
        while c1 or c2:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            v = v1+v2+leftover

            leftover, digit = divmod(v, 10)
            cur.next = ListNode(digit)
            cur = cur.next

            c1 = c1.next if c1 else c1
            c2 = c2.next if c2 else c2
        if leftover:
            cur.next = ListNode(leftover)
        return dummy.next

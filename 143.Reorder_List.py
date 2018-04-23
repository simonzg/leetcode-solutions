# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        fast = head.next.next
        slow = head.next
        slow_pre = head
        while fast and fast.next:
            fast = fast.next.next
            slow_pre = slow
            slow = slow.next
        slow_pre.next = None
        
        cur = slow
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        tail = pre
        a,b = head, tail
        dummy = ListNode(0)
        cur = dummy

        a,b = head,tail
        while a or b:
            if a:
                cur.next = a
                a = a.next
                cur = cur.next
            if b:
                cur.next = b
                b = b.next
                cur = cur.next
        head = dummy.next
        
        
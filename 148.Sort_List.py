# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeList(self, h1, h2):

        dummy = ListNode(0)
        cur = dummy
        while h1 or h2:
            if not h1:
                cur.next = h2
                break
            if not h2:
                cur.next = h1
                break
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
            if cur:
                cur.next = None
        return dummy.next
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        pre = head
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            
        pre.next = None
        
        h1 = self.sortList(head)
        h2 = self.sortList(slow)
        
        return self.mergeList(h1, h2)
        
        
        
        

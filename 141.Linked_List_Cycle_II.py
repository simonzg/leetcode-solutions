"""
Reference: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C++-with-Detailed-Alogrithm-Description

Loop entry point E
Meeting point M
Head H

Let's say the distance between H and E is L1
distance between M and E is L2
because fast pointer traveled twice disance of slow pointer, so

2*(L1+L2) = L1+L2 + n*C
when n=1 (the first meet)
Then L1 = C - L2
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        else:
            return None

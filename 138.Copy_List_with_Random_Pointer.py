'''
REF: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)

Three rounds:
1. append new node right behind original node
2. set random pointer based on original node
3. extract new nodes out to another linked list
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        while cur:
            new_node = RandomListNode(cur.label)
            new_node.next = cur.next
            new_node.random = None
            cur.next = new_node
            cur = new_node.next
        
        cur = head
        while cur:
            if cur.random:
                target = cur.random.next
                node = cur.next
                node.random = target
            cur = cur.next.next
        
        cur = head
        dummy = RandomListNode(0)
        dummy_cur = dummy
        while cur:
            dummy_cur.next = cur.next
            dummy_cur = dummy_cur.next
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
            

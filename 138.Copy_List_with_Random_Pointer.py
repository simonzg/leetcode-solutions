# Hash Table
# time complexity: O(N)
# space complecity: O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ref = {None: None}
        cur = head
        while cur:
            ref[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head
        while cur:
            ref[cur].next = ref[cur.next]
            ref[cur].random = ref[cur.random]
            cur = cur.next
        return ref[head]

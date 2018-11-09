# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums, cur = [], head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums == nums[::-1]
        
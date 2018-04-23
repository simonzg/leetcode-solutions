# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = deque([(root, 0)])
        total = 0
        while (root and queue):
            node, num = queue.popleft()
            base = num*10+node.val
            if not node.left and not node.right:
                total += base
            if node.left:
                queue.append((node.left, base))
            if node.right:
                queue.append((node.right, base))
        return total

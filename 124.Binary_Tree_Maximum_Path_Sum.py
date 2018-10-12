# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = -sys.maxsize-1
        self.dfsMaxPath(root)
        return self.max
    
    def dfsMaxPath(self, node):
        if not node:
            return 0
        l = max(0, self.dfsMaxPath(node.left))
        r = max(0, self.dfsMaxPath(node.right))
        self.max = max(self.max, l+r+node.val)
        return node.val + max(l,r)

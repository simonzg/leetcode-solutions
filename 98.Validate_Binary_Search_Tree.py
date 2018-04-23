# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isValid(root, start, end):
            if root == None:
                return True
            if start < root.val < end:
                return isValid(root.left, start, root.val) and isValid(root.right, root.val, end)
            return False

        return isValid(root, -sys.maxsize, sys.maxsize)

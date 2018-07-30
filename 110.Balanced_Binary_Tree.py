# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            if node.left == None and node.right == None: # is leaf
                return 1
            l, r = check(node.left), check(node.right)
            if l==-1 or r==-1 or abs(l-r)> 1:
                return -1
            return max(l, r) + 1
        
        return check(root) != -1

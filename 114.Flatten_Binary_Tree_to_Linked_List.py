# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Amazing Solution: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return
            
        if root.left:
            cur_left, cur_right = root.left, root.right
            
            pre, cur = cur_left, cur_left.right
            while cur:
                pre = cur
                cur = cur.right
            root.left = None
            root.right = cur_left
            pre.right = cur_right
        
        if root.right:
            self.flatten(root.right)
        

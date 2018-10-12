"""
Reference: https://leetcode.com/problems/binary-search-tree-iterator/discuss/52525/My-solutions-in-3-languages-with-Stack
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = collections.deque()
        self.pushAll(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root and len(self.stack) > 0
        

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val
        
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
            
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

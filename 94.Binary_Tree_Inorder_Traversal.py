# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        stack = [root]
        tmp = root
        while len(stack)>0:
            while tmp != None:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            r.append(tmp.val)
            tmp = tmp.right
        return r






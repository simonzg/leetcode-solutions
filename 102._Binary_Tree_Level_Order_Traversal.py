# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        level = [root]
        result = []

        while root and level:
            result.append([n.val for n in level if n])
            level = [k for node in level for k in (node.left, node.right) if k]
        return result


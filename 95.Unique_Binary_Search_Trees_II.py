# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            trees = []
            for i in range(start, end+1):
                for left in generate(start, i-1):
                    for right in generate(i+1, end):
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees or [None]
        return generate(1,n) if n >= 1 else []

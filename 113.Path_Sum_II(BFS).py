# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        queue, ans = [(root, sum, [])], []
        while queue:
            node, target, path = queue.pop()
            if not node:
                continue
            if target == node.val and not node.left and not node.right:
                ans.append(path+[node.val])
            if node.left:
                queue.append((node.left, target-node.val, path+[node.val]))
            if node.right:
                queue.append((node.right, target-node.val, path+[node.val]))
        return ans

# Collect the path and calculate solution
# time complexity: O(N)
# space complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, v):
            if not node:
                return []
            if node == v:
                return [node]
            lp, rp = dfs(node.left, v), dfs(node.right, v)
            if lp:
                return [node]+lp
            if rp:
                return [node]+rp
            return []

        p1 = dfs(root,  p)
        p2 = dfs(root,  q)

        lmin = min(len(p1), len(p2))
        for i in range(lmin-1, -1, -1):
            if p1[i] == p2[i]:
                return p1[i]
        return 0

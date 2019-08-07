# layered BFS
# time complexity: O(N)
# space complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layer = [root]
        ans = []
        while layer:
            vals, nxt = [], []
            for node in layer:
                if node:
                    vals.append(node.val)
                    nxt.extend([node.left, node.right])
            if vals:
                ans.append(vals)
            layer = nxt
        return ans

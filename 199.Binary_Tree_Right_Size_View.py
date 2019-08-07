# layerd bfs solution
# time complexity: O(N)
# space complexity: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        layer = [root]
        ans = []
        while layer:
            nxt = []
            vals = []
            for node in layer:
                if node:
                    vals.append(node.val)
                    nxt.extend([node.left, node.right])
            if vals:
                ans.append(vals[-1])
            layer = nxt
        return ans

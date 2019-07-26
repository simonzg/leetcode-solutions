# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        layer = [root]
        ans = []
        while layer:
            nxt = []
            vals = []
            for node in layer:
                if node:
                    nxt.extend([node.left, node.right])
                    vals.append(node.val)
            if vals:
                if len(ans) % 2 == 1:
                    ans.append(vals[::-1])
                else:
                    ans.append(vals)
            layer = nxt
        return ans

# Layered BFS
# time complexity: O(N)
# space complexity: O(N)

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
        reverse = False

        while layer:
            vals = []
            nxtLayer = []
            for node in layer:
                vals.append(node.val)
                if node.left:
                    nxtLayer.append(node.left)
                if node.right:
                    nxtLayer.append(node.right)

            if reverse:
                ans.append(vals[::-1])
            else:
                ans.append(vals)

            reverse = not reverse
            layer = nxtLayer
        return ans

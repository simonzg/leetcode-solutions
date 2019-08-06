# Simple BFS with tracking of layer
# time complexity: O(N)
# space complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        leftMost = 0
        queue = [(root, 0)]
        memo = {}
        while queue:
            node, layer = queue.pop(0)

            if node:
                leftMost = min(leftMost, layer)
                memo.setdefault(layer, []).append(node.val)
                queue.extend([(node.left, layer-1), (node.right, layer+1)])
        i = leftMost
        ans = []
        while memo:
            ans.append(memo[i])
            del(memo[i])
            i += 1

        return ans

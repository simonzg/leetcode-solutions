# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        lb, leafs, rb = [], [], []
        if not root:
            return []

        def isLeaf(node):
            return node and not node.left and not node.right

        cur = root.left
        while cur and not isLeaf(cur):
            lb.append(cur.val)
            cur = cur.left if cur.left else cur.right

        cur = root.right
        while cur and not isLeaf(cur):
            rb.append(cur.val)
            cur = cur.right if cur.right else cur.left

        queue = [root.left, root.right]

        while queue:
            node = queue.pop(0)
            if not node:
                continue
            if isLeaf(node):
                leafs.append(node.val)
                continue
            queue.insert(0, node.right)
            queue.insert(0, node.left)

        return [root.val]+lb+leafs+rb[::-1]

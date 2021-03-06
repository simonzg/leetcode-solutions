# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        row, nxt_row = [], [root]
        if not root:
            return
        while nxt_row:
            row, nxt_row = nxt_row, []
            while row:
                node = row.pop(0)
                if node.left:
                    nxt_row.append(node.left)
                if node.right:
                    nxt_row.append(node.right)
                node.next = row[0] if row else None
                
                

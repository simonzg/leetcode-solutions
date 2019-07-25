# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = collections.deque([root])
        ans = []
        while queue:
            node = queue.popleft()
            if not node:
                ans.append('null')
                continue
            ans.append(str(node.val))
            queue.extend([node.left, node.right])
        return '['+','.join(ans)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(data.strip('[]').split(','))
        firstVal = vals.popleft()
        if firstVal == '':
            return None
        root = TreeNode(int(firstVal))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            lv, rv = vals.popleft(), vals.popleft()
            if lv != 'null':
                node.left = TreeNode(int(lv))
                queue.append(node.left)
            if rv != 'null':
                node.right = TreeNode(int(rv))
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

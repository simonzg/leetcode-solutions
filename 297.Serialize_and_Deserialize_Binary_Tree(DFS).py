# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        ans = []

        def dfs(node):
            if node:
                ans.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                ans.append('null')

        dfs(root)
        return '['+','.join(ans)+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(data.strip('[]').split(','))
        if vals[0] == '':
            return None

        def dfs():
            if not vals:
                return None
            v = vals.popleft()
            if v == 'null':
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

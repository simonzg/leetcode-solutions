# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.extend([node.left, node.right])
            else:
                res.append("null")
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        if not vals or vals[0]=='null':
            return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        vals = deque(vals[1:])
        while vals:
            node = q.popleft()
            if vals:
                val = vals.popleft()
                if val != 'null':
                    node.left = TreeNode(int(val))
                    q.append(node.left)
            if vals:
                val = vals.popleft()
                if val != 'null':
                    node.right = TreeNode(int(val))
                    q.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
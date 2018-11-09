# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur_level, nxt_level = [root], []
        res = []
        while cur_level:
            nxt_level = []
            res.append(cur_level[-1].val)
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            cur_level = nxt_level
        return res
            
                
            
        
        
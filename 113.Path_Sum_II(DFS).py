# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, target, path, ans):
            if target == node.val and not node.left and not node.right:
                ans.append(path+[node.val])
                return 

            new_target = target - node.val
            new_path = path+[node.val]
            if node.left:
                dfs(node.left, new_target, new_path, ans)
            if node.right:
                dfs(node.right, new_target, new_path, ans)
        
        ans = []
        if not root:
            return []
        dfs(root, sum, [], ans)
        return ans

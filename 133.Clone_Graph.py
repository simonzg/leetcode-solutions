'''
REF: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).

The Best
'''
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import collections
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, root):
        if not root:
            return 
        
        dic = {root: UndirectedGraphNode(root.label)}
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node_copy = dic[node]
            
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    dic[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                
                node_copy.neighbors.append(dic[neighbor])
        return dic[root]
 

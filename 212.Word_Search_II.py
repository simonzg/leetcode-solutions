"""
Reference: https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
"""
from collections import defaultdict
    
class Trie():
    def __init__(self):
        self.root = defaultdict()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.setdefault(w, {})
        node['leaf'] = True
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if 'leaf' in node and node['leaf']:
            res.append(path)
            node['leaf'] = False
            # notice there should be no return
            # since one word end doesn't mean the search should end
            # examples could be bend & benda
            # when search for bend ends
            # the dfs should continue to look for benda
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        ch = board[i][j]
        
        board[i][j] = "#"
        nextNode = node.get(ch)
        if nextNode:
            self.dfs(board, nextNode, i-1, j, path+ch, res)
            self.dfs(board, nextNode, i+1, j, path+ch, res)
            self.dfs(board, nextNode, i, j-1, path+ch, res)
            self.dfs(board, nextNode, i, j+1, path+ch, res)
        board[i][j] = ch
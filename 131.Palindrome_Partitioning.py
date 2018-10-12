class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        
        for i in range(1,len(s)+1):
            word = s[:i]
            if word[::-1] == word:
                self.dfs(s[i:], path+[word], res)

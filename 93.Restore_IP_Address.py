class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], 4, res)
        return res

    def dfs(self, leftover, path, depth, res):
        if depth == 0:
            if not leftover:
                res.append('.'.join(path))
            return



        if len(leftover) >= 1:
            self.dfs(leftover[1:], path+[leftover[:1]], depth-1, res)
        if len(leftover) >= 2 and leftover[0] != '0':
            self.dfs(leftover[2:], path+[leftover[:2]], depth-1, res)
        if len(leftover) >= 3 and leftover[0] != '0' and int(leftover[:3]) <= 255:
            self.dfs(leftover[3:], path+[leftover[:3]], depth-1, res)



# DFS with memorization
# O(N^2)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = {}
        for w in wordDict:
            dic.setdefault(w[0], []).append(w)
        memo = {}

        def dfs(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]
            ch = s[0]
            for prefix in dic.get(ch, []):
                if prefix == s[:len(prefix)]:
                    if dfs(s[len(prefix):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False

        return dfs(s)

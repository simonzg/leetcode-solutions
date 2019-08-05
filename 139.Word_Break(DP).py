# DP with this definition:
# dp[i] = True if s[0:i] is breakable string
# dp[i] = True if dp[j] == True and s[j:i] in wordDict
#
# time complexity: O(N^2)
# space complexity: O(N)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):  # notice the n+1 here
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

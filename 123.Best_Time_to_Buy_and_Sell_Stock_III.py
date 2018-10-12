# DP
# dp[k,i] = max(dp[k,i-1], prices[i]-prices[j]+dp[k-1,j-1]) j in [0..i-1]
# reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*n for i in range(3)]
        for k in range(1,3):
            m = prices[0]
            for i in range(1,n):
                m = min(m, prices[i]-dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i]-m)
        return dp[2][n-1]

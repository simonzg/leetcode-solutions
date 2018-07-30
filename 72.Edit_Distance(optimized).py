# O(n) space (row-based iteration)
# refrence: https://leetcode.com/problems/edit-distance/discuss/25846/20ms-Detailed-Explained-C++-Solutions-(O(n)-Space)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        pre = [i for i in range(n+1)]
        for i in range(1, m+1):
            cur = [0 for i in range(n+1)]
            cur[0] = i
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = pre[j-1]
                else:
                    cur[j] = min(cur[j-1], pre[j], pre[j-1]) + 1
            pre = cur
        return pre[n]
                    
                    

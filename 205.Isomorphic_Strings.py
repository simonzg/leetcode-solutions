"""
Reference: https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
"""
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        if ls != lt:
            return False
        d = {}
        for i in range(ls):
            ch_s, ch_t = s[i], t[i]
            if ch_s in d and d[ch_s] != ch_t:
                return False
            if ch_s not in d and ch_t in d.values():
                return False
    
            d[ch_s] = ch_t
        return True
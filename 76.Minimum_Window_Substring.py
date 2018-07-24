import collections
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        i=l=r=0
        for j,ch in enumerate(s,1):
            missing -= need[ch] >0
            need[ch] -= 1
            if not missing:
                while i<j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i+=1
                if not r or j-i <= r-l:
                    l,r = i,j
        return s[l:r]
                

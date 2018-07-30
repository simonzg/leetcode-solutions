class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m,n = len(s1), len(s2)
        if m!=n or sorted(s1) != sorted(s2):
            return False
        if m<=3 or s1==s2:
            return True
        for i in range(1,n):
            f = self.isScramble
            if ((f(s1[:i], s2[:i]) and f(s1[i:], s2[i:])) or \
                (f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]))):
                return True
        return False

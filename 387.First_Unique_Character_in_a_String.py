class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        visited = []
        for i,ch in enumerate(s):
            if ch in visited:
                continue
            if ch not in s[i+1:]:
                return i
            else:
                visited.append(ch)
        return -1

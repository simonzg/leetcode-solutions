class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur = reduce(lambda s,d: s*10+d, digits, 0)
        nxt = cur + 1
        return [int(ch) for ch in str(nxt)]

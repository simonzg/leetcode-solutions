class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n:
            if n == 1:
                return True
            if n % 2 == 0 and n > 1:
                n >>= 1
            else:
                return False
        return False
            

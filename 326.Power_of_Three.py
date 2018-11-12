class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n == 1:
                return True
            if n % 3 == 0 and n > 1:
                n //= 3
            else:
                break
        return False

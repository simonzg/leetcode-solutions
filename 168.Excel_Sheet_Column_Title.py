class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        chList = [chr(ord('A')+i) for i in range(26)]
        ans = ''
        while n:
            i,n  = n%26, n//26
            
            if not i:
                i = 26 if n >0 else 0
                n -= 1
            ans = chList[i-1] + ans
            
        return ans

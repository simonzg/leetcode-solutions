class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = "1"
        for i in range(n-1):
            new_r = ''
            val = r[0]
            cnt = 0
            for d in r:
                if d == val:
                    cnt +=1
                else:
                    new_r += str(cnt)+val
                    cnt = 1
                    val = d
            new_r += str(cnt)+d
            r = new_r
        return ''.join(r)
            
        

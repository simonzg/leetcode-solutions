class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        adv = 0
        r = []
        a = list(a)
        b = list(b)
        while a or b:
            va = int(a.pop()) if a else 0
            vb = int(b.pop()) if b else 0
            v = va+vb+adv
            r.insert(0, str(v%2))
            adv = v//2
        if adv != 0:
            r.insert(0, str(adv))
        return ''.join(r)
        
        

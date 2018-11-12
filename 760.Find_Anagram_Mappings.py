class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        
        for i,n in enumerate(B):
            dic.setdefault(n, []).append(i)
        
        
        return [dic.get(n).pop(0) for n in A]
